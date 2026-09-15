import re, glob, os

files = sorted(glob.glob(r"D:\+Python\Novel-Wen-Wen\第一卷\第*章_*_正文_v1.md"))
out = []
for f in files:
    name = os.path.basename(f)
    m = re.match(r"第(\d+)章", name)
    if not m:
        continue
    n = int(m.group(1))
    if n < 4:
        continue
    lines = open(f, encoding="utf-8").read().split("\n")
    body = "\n".join(l for l in lines if not l.startswith("# "))
    han = len(re.findall(r"[\u4e00-\u9fff]", body))
    nb = len(re.sub(r"\s", "", body))
    ok = "OK" if 2800 <= han <= 3300 else "OUT"
    out.append("ch%d han=%d nonspace=%d %s" % (n, han, nb, ok))

open(r"D:\+Python\Novel-Wen-Wen\.workbuddy\tmp\count3.txt", "w", encoding="utf-8").write("\n".join(out))
print("done")
