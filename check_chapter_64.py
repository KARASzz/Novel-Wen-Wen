#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def check_chapter(filename, chapter_num):
    """检查章节的字数、章号泄漏、半角标点、句式"""
    
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 按状态账本分割
    parts = text.split('## 状态账本')
    main_text = parts[0]
    
    # 1. 统计汉字数
    hanzi = re.findall(r'[\u4e00-\u9fff]', main_text)
    hanzi_count = len(hanzi)
    print(f"第{chapter_num}章汉字数：{hanzi_count}")
    if 2800 <= hanzi_count <= 3300:
        print(f"  ✓ 字数在2800-3300范围内")
    elif hanzi_count < 2800:
        print(f"  ✗ 字数不足，还差 {2800 - hanzi_count} 字")
    else:
        print(f"  ✗ 字数超标，超出 {hanzi_count - 3300} 字")
    
    # 2. 检查章号泄漏
    # 排除"第64章"（标题）和"第1-3章"等版本号
    chapter_pattern = r'第\s*(\d+)\s*章'
    matches = re.finditer(chapter_pattern, main_text)
    leaks = []
    for m in matches:
        num = int(m.group(1))
        # 排除版本号（如"第1-3章"）
        context_start = max(0, m.start() - 10)
        context = main_text[context_start:m.end()]
        if '-' in context or 'v' in context.lower():
            continue
        # 排除本章标题
        if num == chapter_num:
            continue
        leaks.append(m.group(0))
    
    if leaks:
        print(f"\n⚠ 发现章号泄漏：{', '.join(leaks)}")
    else:
        print(f"\n✓ 无章号泄漏")
    
    # 3. 检查半角标点
    half_width = re.findall(r'[,;:!?]', main_text)
    if half_width:
        print(f"\n⚠ 发现半角标点：{len(half_width)} 处")
        # 显示前5处
        for i, m in enumerate(re.finditer(r'[,;:!?]', main_text)):
            if i >= 5:
                break
            context_start = max(0, m.start() - 10)
            context_end = min(len(main_text), m.end() + 10)
            context = main_text[context_start:context_end].replace('\n', ' ')
            print(f"  {i+1}. ...{context}...")
    else:
        print(f"\n✓ 无半角标点")
    
    # 4. 检查"不是...是..."句式
    pattern = r'不是[^，。！？\n]{1,30}是[^，。！？\n]{1,30}'
    matches = re.findall(pattern, main_text)
    if len(matches) > 2:
        print(f"\n⚠ 「不是…是…」句式：{len(matches)} 处（建议≤2）")
        for i, m in enumerate(matches[:5]):
            print(f"  {i+1}. {m}")
    else:
        print(f"\n✓ 「不是…是…」句式：{len(matches)} 处")
    
    return hanzi_count, len(leaks) > 0, len(half_width) > 0, len(matches) > 2

if __name__ == '__main__':
    check_chapter('第二卷/第64章_旧东西不该在黑市_正文_v1.md', 64)
