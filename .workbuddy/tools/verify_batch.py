# -*- coding: utf-8 -*-
"""整批改稿验收（只读）。

用法：
  python3 .workbuddy/tools/verify_batch.py            # 校验全部 80 章有效正文
  python3 .workbuddy/tools/verify_batch.py --new      # 只校验本轮新版本文件
  python3 .workbuddy/tools/verify_batch.py --locked   # 另跑原话锁定表

口径与项目一致：
  汉字 = [一-鿿]，不含章标题、标点、数字、字母、空白、Markdown、文末附录。
"""
import argparse
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PUB = os.path.join(ROOT, "正式待发表")
BASELINE = os.path.join(PUB, "审稿", "第1-80章_审稿基线_v1.json")

DIR_WORDS = re.compile(r"第一卷|第二卷|本卷|上一卷|分卷大纲|章纲")
CHAP_NUM = re.compile(r"第\s*\d+\s*章")
HALF = re.compile(r"[,;:!?()]")
# 「清单」在正文里多数是故事内词（补给清单／损失清单），单列出来人工判断，不直接判失败
LIST_WORD = re.compile(r"清单")

# 原话—引用章锁定表：锁定句必须逐字仍在
LOCKED = [
    (25, "不要问他是不是霸主文明"),
    (26, "这里比我想的还要干净"),
    (27, "我就这一件"),
    (39, "我真不是霸主文明"),
    (53, "我就这一件"),
    (70, "我们已经按照霸主使者要求交出三座城市的能源核心。"),
    (70, "请问审判舰什么时候放过我们？"),
    (73, "伪协议事件·权限响应不完整·来源不明。"),
    (74, "压不动"),
]


def body_of(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    i = text.find("\n## ")
    while i != -1 and text[i + 1:i + 6].startswith("## 正文"):
        end = text.find("\n", i + 1)
        text = text[:i] + text[end:]
        i = text.find("\n## ")
    if i != -1:
        text = text[:i]
    return "\n".join(
        l for l in text.split("\n")
        if not re.match(r"^#*\s*第\d+章[：:]", l) and not re.match(r"^#+\s*《", l)
    )


def hanzi(text):
    return len(re.findall(r"[一-鿿]", text))


def report(path):
    txt = body_of(path)
    name = os.path.basename(path)
    issues = []
    n = hanzi(txt)
    if not (2800 <= n <= 3300):
        issues.append("字数 %d 不在 2800—3300" % n)
    dq = txt.count('"')
    if dq:
        issues.append('英文直引号 %d' % dq)
    bt = txt.count("`")
    if bt:
        issues.append("反引号 %d" % bt)
    half = HALF.findall(txt)
    if half:
        issues.append("半角标点 %d %s" % (len(half), sorted(set(half))))
    dw = DIR_WORDS.findall(txt)
    if dw:
        issues.append("目录用语 %s" % dw[:4])
    cn = CHAP_NUM.findall(txt)
    if cn:
        issues.append("章号泄漏 %s" % cn[:4])
    notes = []
    if LIST_WORD.findall(txt):
        notes.append("「清单」x%d（人工判是故事内词还是目录用语）" % len(LIST_WORD.findall(txt)))
    return n, issues, notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--new", action="store_true", help="只查本轮新版本")
    ap.add_argument("--locked", action="store_true", help="另跑原话锁定表")
    args = ap.parse_args()

    with open(BASELINE, encoding="utf-8") as f:
        data = json.load(f)
    rows = []
    if args.new:
        for path in sorted(glob.glob(os.path.join(PUB, "第*章*_正文_v*.md"))):
            base = os.path.basename(path)
            if base in {os.path.basename(c["single"]) for c in data["chapters"]}:
                continue  # 旧有效稿
            rows.append(path)
    else:
        rows = [os.path.join(ROOT, c["single"]) for c in data["chapters"]]

    bad = 0
    for path in rows:
        n, issues, notes = report(path)
        flag = "OK  " if not issues else "FAIL"
        if issues:
            bad += 1
        print("%s %-44s %5d  %s" % (flag, os.path.basename(path), n,
                                    "；".join(issues + notes)))
    print("---")
    print("检查 %d 章，有问题 %d 章" % (len(rows), bad))

    if args.locked:
        print()
        print("== 原话锁定表 ==")
        for ch, frag in LOCKED:
            hit = False
            for c in data["chapters"]:
                if c["chapter"] != ch:
                    continue
                p = os.path.join(ROOT, c["single"])
                new = os.path.join(PUB, re.sub(r"_v(\d+)\.md$",
                          lambda m: "_v%d.md" % (int(m.group(1)) + 1), os.path.basename(p)))
                for cand in (p, new):
                    if os.path.exists(cand) and frag in open(cand, encoding="utf-8").read():
                        hit = True
            print("%s ch%-3d %s" % ("OK  " if hit else "MISS", ch, frag))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
