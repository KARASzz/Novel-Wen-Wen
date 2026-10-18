"""本轮合订稿定点修订工具；以工作状态哈希防止覆盖外部修改。"""
from pathlib import Path
import hashlib
import json
import re

SOURCE = Path('正式待发表/《我真不是霸主文明》1-80.txt')
STATE = Path('正式待发表/审稿/第1-80章_资料适配工作状态_v1.json')
state = json.loads(STATE.read_text(encoding='utf-8'))
raw = SOURCE.read_bytes()
assert hashlib.sha256(raw).hexdigest() == state['current_sha256']
text = raw.decode('utf-8')
heads = list(re.finditer(r'^第\s*(\d+)\s*章[^\r\n]*', text, re.M))
chapters = {i+1: text[h.start():heads[i+1].start() if i < 79 else len(text)]
            for i, h in enumerate(heads)}

def patch(n, old, new, reason):
    old = old.replace('\r\n', '\n').replace('\n', '\r\n')
    new = new.replace('\r\n', '\n').replace('\n', '\r\n')
    assert chapters[n].count(old) == 1, (n, old, chapters[n].count(old))
    chapters[n] = chapters[n].replace(old, new, 1)
    state['chapters'][str(n)]['edits'].append(dict(old=old, new=new, reason=reason))

def finish(numbers, note):
    for n in numbers:
        count = len(re.findall(r'[\u4e00-\u9fff]', chapters[n].split('\n', 1)[1]))
        assert 2800 <= count <= 3300, (n, count)
        state['chapters'][str(n)].update(reviewed=True, current_hanzi=count, review_note=note)
        print(n, count)
    out = (state['preamble'] + ''.join(chapters.values())).encode('utf-8')
    assert b'\n' not in out.replace(b'\r\n', b'')
    SOURCE.write_bytes(out)
    state.update(current_sha256=hashlib.sha256(out).hexdigest(), last_reviewed=max(numbers), next_chapter=max(numbers)+1)
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')
