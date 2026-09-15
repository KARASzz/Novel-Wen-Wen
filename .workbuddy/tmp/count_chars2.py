import re

def count(path, tag):
    t = open(path, encoding="utf-8").read()
    cut = t.find("## v2 修订记录")
    if cut > 0:
        t = t[:cut]
    idx = [m.start() for m in re.finditer(r"^# 第\d章", t, re.M)]
    idx.append(len(t))
    out = []
    for i in range(len(idx) - 1):
        seg = t[idx[i]:idx[i+1]]
        han = len(re.findall(r"[\u4e00-\u9fff]", seg))
        nb = len(re.sub(r"\s", "", seg))
        out.append("ch%d han=%d nonspace=%d" % (i + 1, han, nb))
    han = len(re.findall(r"[\u4e00-\u9fff]", t))
    nb = len(re.sub(r"\s", "", t))
    out.append("total han=%d nonspace=%d" % (han, nb))
    return tag + " | " + " | ".join(out)

lines = []
lines.append(count(r"D:\+Python\Novel-Wen-Wen\第一卷\第1-3章_正文_v1.md", "V1"))
lines.append(count(r"D:\+Python\Novel-Wen-Wen\第一卷\第1-3章_正文_v2.md", "V2"))
open(r"D:\+Python\Novel-Wen-Wen\.workbuddy\tmp\count2.txt", "w", encoding="utf-8").write("\n".join(lines))
print("done")
