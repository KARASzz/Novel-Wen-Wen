import re
path = r'D:\+Python\Novel-Wen-Wen\第二卷\第50章_旧工作服的意义_正文_v1.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    ('——**这是你的判断**——**不是他说的**。', '——**这是你的判断**——**他说不出来这种话**。'),
    ('——**铺垫**——**不是写出来的**——**是事实**——', '——**铺垫**——**靠的是事实**——'),
    ('——**不是"生态单元和机械单元"**——**是他**——**他在修**。',
     '——**画面里的人**——**是他**——**他在修**。'),
]

for old, new in replacements:
    if old in text:
        text = text.replace(old, new)
        print(f'  ✓ 替换: {old[:30]}')
    else:
        print(f'  ✗ 没找到: {old[:30]}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
