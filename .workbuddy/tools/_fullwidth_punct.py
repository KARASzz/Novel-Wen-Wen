# -*- coding: utf-8 -*-
"""一次性脚本:把指定章节文件正文中所有半角标点替换为全角。"""
import sys

path = sys.argv[1]
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('\n## ')
head = text[:idx]
tail = text[idx:] if idx != -1 else ''

# ASCII -> 全角 (使用 unicode codepoint,不用字面量)
mapping = [
    (ord(','), '，'),  # 半角逗号 -> 全角
    (ord(';'), '；'),
    (ord(':'), '：'),
    (ord('?'), '？'),
    (ord('!'), '！'),
    (ord('('), '（'),
    (ord(')'), '）'),
]

for k, v in mapping:
    head = head.replace(chr(k), v)

# 双引号配对
out = []
in_pair = False
for ch in head:
    if ch == '"':
        if not in_pair:
            out.append('“')
            in_pair = True
        else:
            out.append('”')
            in_pair = False
    else:
        out.append(ch)
head = ''.join(out)

with open(path, 'w', encoding='utf-8') as f:
    f.write(head + tail)
print('OK')