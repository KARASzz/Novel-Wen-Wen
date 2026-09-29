# write_chapter.py
"""标准写章流水线:每章以 heredoc 写入,然后自动校验。

用法:
1. 复制本模板到目标章文件
2. 改章号和正文
3. 运行校验

校验项:
- 字数 2800—3300
- 半角标点 0
- 「不是…是…」句式统计
- 章号泄漏 0(正文里)
"""
import re
import sys

if len(sys.argv) < 2:
    print('Usage: python write_chapter.py <file>')
    sys.exit(1)

f = sys.argv[1]
with open(f, 'r', encoding='utf-8') as fp:
    text = fp.read()

# 替换半角标点
text = text.replace(',', '，').replace(';', '；').replace('?', '？').replace('!', '！')
with open(f, 'w', encoding='utf-8') as fp:
    fp.write(text)

# 切分正文
cut = text.find('\n## ')
body = text[:cut] if cut > 0 else text
lines = body.split('\n', 1)
body = lines[1] if len(lines) > 1 else body

n = len(re.findall(r'[一-鿿]', body))
matches = re.findall(r'[,;?!]', body)
matches3 = re.findall(r'不是.*?是', body)
matches4 = re.findall(r'第\d+章', body)

print(f'{f}: {n} 字 | 半角{len(matches)} | 不是…是…{len(matches3)} | 章号泄漏{len(matches4)}')

if n < 2800:
    print(f'  ⚠ 字数不足(差{2800-n})')
elif n > 3300:
    print(f'  ⚠ 字数超标(超{n-3300})')
else:
    print('  ✓ 字数达标')