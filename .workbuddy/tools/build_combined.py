# -*- coding: utf-8 -*-
"""从 正式待发表/ 单章正文重建合订稿《我真不是霸主文明》1-80.txt。

合订稿是给平台投递用的排版稿，规则（对照作者手工排版后的既有快照还原）：
  1. 每章开头一行 `第N章_标题_正文_vM`（就是单章文件名去掉 .md），空一行；
  2. 下一行 `第N章：标题` 与正文第一句同段；
  3. 正文按句断行，一句一行，不保留段落空行（场景切换用空行分开）；
  4. 破折号 `——` 改句号（平台正文不显示破折号）；
  5. 章节之间空一行。
用法：python3 .workbuddy/tools/build_combined.py --check
      python3 .workbuddy/tools/build_combined.py --write
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PUB = os.path.join(ROOT, "正式待发表")
MASTER = os.path.join(PUB, "《我真不是霸主文明》1-80.txt")
BASELINE = os.path.join(PUB, "审稿", "第1-80章_审稿基线_v1.json")

SENT_END = "。！？"


def chapter_list():
    with open(BASELINE, encoding="utf-8") as f:
        data = json.load(f)
    return [(c["chapter"], c["single"]) for c in data["chapters"]]


def body_of(path):
    """单章正文：去掉 markdown 标题行与文末空行。"""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    lines = [l for l in text.split("\n") if not re.match(r"^#*\s*第\d+章[：:]", l)]
    lines = [l for l in lines if l.strip()]
    return "\n".join(lines)


def title_of(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            m = re.match(r"^#*\s*第(\d+)章[：:]\s*(.+?)\s*$", line.strip())
            if m:
                return int(m.group(1)), m.group(2)
            break
    raise SystemExit("章标题行读不出：%s" % path)


def stem_of(path, num, title):
    """合订稿里的章节抬头：第N章_标题_正文_vM（单章文件名不带标题的补齐）。"""
    base = os.path.basename(path)[: -len(".md")]
    m = re.match(r"^第(\d+)章_正文_(v\d+)$", base)
    if m:
        return "第%d章_%s_%s" % (num, title, m.group(2))
    return base


def split_sentences(text):
    """一句一行。

    断行规则（对照作者手工排版后的既有合订稿还原）：
      · 引号外的句末标点后断行；
      · 引号内的句末标点不断行；
      · 收尾引号紧跟句末标点时，断在这一行末尾。
    """
    out = []
    buf = []
    depth = 0
    openers = "“「『【"
    closers = "”」』】"
    for ch in text:
        if ch in openers:
            depth += 1
        elif ch in closers:
            depth = max(0, depth - 1)
        buf.append(ch)
        brk = ch in SENT_END and depth == 0
        if ch in closers and depth == 0 and len(buf) > 1 and buf[-2] in SENT_END:
            brk = True
        if brk:
            out.append("".join(buf).strip())
            buf = []
    tail = "".join(buf).strip()
    if tail:
        out.append(tail)
    return [s for s in out if s]


def render(chapters):
    blocks = ["《我真不是霸主文明》", ""]
    for num, rel in chapters:
        path = os.path.join(ROOT, rel)
        title = title_of(path)[1]
        stem = stem_of(path, num, title)
        body = body_of(path)
        body = body.replace("——", "。")
        body = body.replace("**", "")
        body = re.sub(r"。{2,}", "。", body)
        sents = []
        for para in body.split("\n"):
            sents.extend(split_sentences(para))
        if not sents:
            raise SystemExit("空章：%s" % rel)
        lines = [stem, "", "第%d章：%s %s" % (num, title, sents[0])]
        lines += sents[1:]
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    out = render(chapter_list())
    if args.write:
        with open(MASTER, "w", encoding="utf-8") as f:
            f.write(out)
        print("已重建：%s" % MASTER)
        return 0
    with open(MASTER, encoding="utf-8") as f:
        cur = f.read()
    if cur == out:
        print("与现有合订稿逐字一致。")
        return 0
    import difflib

    a = cur.split("\n")
    b = out.split("\n")
    print("现有 %d 行 / 重建 %d 行" % (len(a), len(b)))
    n = 0
    for line in difflib.unified_diff(a, b, "现有", "重建", n=1, lineterm=""):
        n += 1
        if n > 120:
            print("...（差异过多，已截断）")
            break
        print(line)
    return 1


if __name__ == "__main__":
    sys.exit(main())
