import re, io, sys

path = r"D:\+Python\Novel-Wen-Wen\第一卷\第1-3章_正文_v1.md"
text = io.open(path, encoding="utf-8").read()

# split by chapter headings
parts = re.split(r"\n# (第\d+章：[^\n]+)\n", text)
# parts[0] is preamble
chapters = []
for i in range(1, len(parts), 2):
    chapters.append((parts[i], parts[i+1]))

def count(body):
    # strip scene separators
    b = body.replace("---", "")
    cjk = len(re.findall(r"[\u4e00-\u9fff]", b))
    total = len(re.sub(r"\s", "", b))
    return cjk, total

for title, body in chapters:
    cjk, total = count(body)
    print(f"{title}\t中文字符={cjk}\t非空白字符={total}")

# whole book
cjk, total = count(text)
print(f"全篇\t中文字符={cjk}\t非空白字符={total}")
