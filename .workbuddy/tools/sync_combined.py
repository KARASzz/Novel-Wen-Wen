# -*- coding: utf-8 -*-
"""把本轮修订的单章同步进合订稿，只替换被改的章，其余章逐字不动。

合订稿 `正式待发表/《我真不是霸主文明》1-80.txt` 是作者手工排版的投递稿：
一句一行、破折号改句号、去 markdown 粗体。它不是脚本产物，全量重建会破坏
作者的手工排版，所以这里只做**定点替换**。

用法：
  python3 .workbuddy/tools/sync_combined.py --dry     # 只报告将要替换的章
  python3 .workbuddy/tools/sync_combined.py --apply    # 实际写入（先写 .bak）
"""
import argparse
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_combined import body_of, split_sentences, title_of  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PUB = os.path.join(ROOT, "正式待发表")
MASTER = os.path.join(PUB, "《我真不是霸主文明》1-80.txt")
BACKUP = MASTER + ".bak"

STEM = re.compile(r"^第(\d+)章_.+_v(\d+)$")


def new_file_for(stem):
    """合订稿抬头 `第N章_标题_正文_vM` → 目录里是否存在递增一版的新文件。"""
    m = re.match(r"^第(\d+)章_.*_v(\d+)$", stem)
    if not m:
        return None
    nxt = int(m.group(2)) + 1
    cands = ["%s_v%d.md" % (stem[: stem.rfind("_v")], nxt)]
    # 第 1—3 章的单章文件名不带标题（`第2章_正文_v3.md`），按章号再找一次
    cands.append("第%s章_正文_v%d.md" % (m.group(1), nxt))
    for c in cands:
        if os.path.exists(os.path.join(PUB, c)):
            return c
    return None


def render(path):
    title = title_of(path)[1]
    base = os.path.basename(path)[: -len(".md")]
    body = body_of(path)
    body = body.replace("——", "。").replace("**", "")
    body = re.sub(r"。{2,}", "。", body)
    sents = []
    for para in body.split("\n"):
        sents.extend(split_sentences(para))
    num = int(re.match(r"^第(\d+)章", base).group(1))
    return "\n".join([base, "", "第%d章：%s %s" % (num, title, sents[0])] + sents[1:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    if not (args.dry or args.apply):
        ap.error("必须指定 --dry 或 --apply")

    with open(MASTER, encoding="utf-8") as f:
        lines = f.read().split("\n")

    starts = []
    for i, l in enumerate(lines):
        m = STEM.match(l)
        if m:
            starts.append((i, int(m.group(1))))

    revised = {}
    for idx, (i, num) in enumerate(starts):
        stem = lines[i]
        cand = new_file_for(stem)
        if cand is None:
            continue
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)
        while end - 1 > i and lines[end - 1].strip() == "":
            end -= 1
        revised[num] = (i, end, cand, stem)

    print("合订稿 %d 章，其中 %d 章有新版本待同步：" % (len(starts), len(revised)))
    for num in sorted(revised):
        i, end, cand, stem = revised[num]
        head = lines[i + 2]
        old_body = re.sub(r"^第\d+章[：:][^\n]*?[\s]?", "", head, count=1) + "\n" + "\n".join(lines[i + 3:end])
        old_n = len(re.findall(r"[一-鿿]", old_body))
        new_n = len(re.findall(r"[一-鿿]", body_of(os.path.join(PUB, cand))))
        print("  第%2d章 %s → %s   汉字 %d → %d   行 %d → ?" % (num, stem, cand, old_n, new_n, end - i))

    if args.dry:
        return 0

    if not revised:
        print("没有需要同步的章。")
        return 0
    shutil.copyfile(MASTER, BACKUP)
    for num in sorted(revised, reverse=True):
        i, end, cand, _ = revised[num]
        lines[i:end] = render(os.path.join(PUB, cand)).split("\n")
    with open(MASTER, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("已同步 %d 章；原文件已备份到 %s" % (len(revised), os.path.basename(BACKUP)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
