# -*- coding: utf-8 -*-
"""章节交付前自检（对齐项目系统指令的「AI 写稿自检五条」部分项）。
检查范围仅正文：截掉第一个 '## ' 起的状态账本/修订记录。
1) 章号泄漏：正文里出现「第N章」
2) 半角标点：正文里出现 , . ; : ! ? ( ) 等半角符号
3) 「不是…是…」句式计数（句内共现）
"""
import re
import sys
import os

D = r"D:\+Python\Novel-Wen-Wen\第一卷"


def body_of(path):
    t = open(path, encoding="utf-8").read()
    # `## 正文` 是正文段头，不算正文也不算分段；其余第一个 `## ` 起的内容截掉。
    i = t.find("\n## ")
    while i != -1 and t[i + 1:i + 6].startswith("## 正文"):
        line_end = t.find("\n", i + 1)
        t = t[:i] + t[line_end:]
        i = t.find("\n## ")
    if i != -1:
        t = t[:i]
    return "\n".join(
        l for l in t.split("\n")
        if not re.match(r"^#\s*第", l) and not re.match(r"^#\s*《", l)
    )


def pairs(txt):
    n = 0
    for s in re.split(r"[。！？\n]", txt):
        if "不是" in s and re.search(r"不是[^，、]{0,30}?[，,]?\s*是", s):
            n += 1
    return n


if __name__ == "__main__":
    for a in sys.argv[1:]:
        p = a if os.path.isabs(a) else os.path.join(D, a)
        txt = body_of(p)
        zh = re.findall(r"第\d+章", txt)
        half = re.findall(r"[,;:!?()\"]", txt)
        print(f"{os.path.basename(p)}")
        print(f"   章号泄漏: {len(zh)} {zh[:6]}")
        print(f"   半角标点: {len(half)} {sorted(set(half))}")
        print(f"   不是…是…句式: {pairs(txt)}   含「不是」句: {len(re.findall('不是', txt))}")
