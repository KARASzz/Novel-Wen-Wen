# -*- coding: utf-8 -*-
"""章节字数与句式统计。
口径（见台账）：正文汉字数 = 不含章标题、标点、数字字母、状态账本段、修订记录段。
算法：先截掉第一个 '## ' 起的内容 → 去掉章标题行 → 数 [\u4e00-\u9fff]。
"""
import re
import sys
import os

D = r"D:\+Python\Novel-Wen-Wen\第一卷"


def _body(t):
    """截掉正文之外的分段。
    规则：`## 正文` 是正文段头（不算正文，也不截断）；其余第一个 `## ` 起的
    内容（状态账本／修订记录等）一律截掉。
    """
    i = t.find("\n## ")
    while i != -1:
        seg = t[i + 1:i + 6]
        if seg.startswith("## 正文"):
            # 只删掉这一行，继续往后找真正的分段
            line_end = t.find("\n", i + 1)
            t = t[:i] + t[line_end:]
            i = t.find("\n## ")
            continue
        break
    if i != -1:
        t = t[:i]
    return t


def stats(path):
    t = open(path, encoding="utf-8").read()
    body = _body(t)
    lines = []
    for l in body.split("\n"):
        if re.match(r"^#\s*第", l):
            continue
        if re.match(r"^#\s*《", l):
            continue
        lines.append(l)
    txt = "\n".join(lines)
    n = len(re.findall(r"[\u4e00-\u9fff]", txt))
    bushi = len(re.findall(r"不是", txt))
    return n, bushi


def show_lines(path):
    t = open(path, encoding="utf-8").read()
    i = t.find("\n## ")
    body = t[:i] if i != -1 else t
    for k, l in enumerate(body.split("\n")):
        if "不是" in l or "是…" in l:
            print(f"  L{k+1:<4} {l.strip()}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--lines"]
    lines_mode = "--lines" in sys.argv
    if not args:
        print("usage: count_chapter.py [--lines] <file> [<file> ...]", file=sys.stderr)
        sys.exit(1)
    for a in args:
        p = a if os.path.isabs(a) else os.path.join(D, a)
        n, b = stats(p)
        flag = "" if 2800 <= n <= 3300 else "  <<< OUT OF RANGE"
        print(f"{os.path.basename(p):<48} {n:>6}  bu-shi={b}{flag}")
        if lines_mode:
            show_lines(p)
