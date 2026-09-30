# -*- coding: utf-8 -*-
"""改稿收尾后刷新审稿基线 JSON（原稿源哈希 → 新版 + 合订稿哈希 + 逐章只读字数）。

用法：python3 .workbuddy/tools/refresh_baseline.py --apply
不带 --apply 只打印将要写入的内容摘要。
"""
import argparse
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PUB = os.path.join(ROOT, "正式待发表")
SRC = os.path.join(PUB, "审稿", "第1-80章_审稿基线_v1.json")
BASELINE = os.path.join(PUB, "审稿", "第1-80章_审稿基线_v2.json")
MASTER = os.path.join(PUB, "《我真不是霸主文明》1-80.txt")


def stats(path):
    """字数一律走项目自带的 count_chapter.py，避免第二套口径。"""
    import importlib.util
    spec = importlib.util.spec_from_file_location("cc", os.path.join(ROOT, ".workbuddy/tools/count_chapter.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.stats(path)[0]


def body_of(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    i = text.find("\n## ")
    if i != -1:
        text = text[:i]
    return "\n".join(
        l for l in text.split("\n")
        if not re.match(r"^#*\s*第\d+章[：:]", l) and not re.match(r"^#+\s*《", l) and l.strip()
    )


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    with open(SRC, encoding="utf-8") as f:
        data = json.load(f)

    total = 0
    lo = hi = None
    print("章  有效正文文件（新版本）                              汉字")
    for c in data["chapters"]:
        single = c["single"]
        path = os.path.join(ROOT, single)
        old_v = re.search(r"_v(\d+)\.md$", os.path.basename(single))
        cand = os.path.join(
            os.path.dirname(path),
            re.sub(r"_v(\d+)\.md$", lambda m: "_v%d.md" % (int(m.group(1)) + 1),
                   os.path.basename(single)),
        )
        if os.path.exists(cand):
            c["single"] = os.path.relpath(cand, ROOT)
            c["replaces"] = single
            c.pop("matches", None)
            c.pop("body_hanzi", None)
            c.pop("combined_start_line", None)
            c.pop("combined_end_line", None)
        n = stats(os.path.join(ROOT, c["single"]))
        c["body_hanzi"] = n
        c["in_range"] = 2800 <= n <= 3300
        total += n
        lo = n if lo is None else min(lo, n)
        hi = n if hi is None else max(hi, n)
        print("%-4d %-48s %5d %s" % (c["chapter"], os.path.basename(c["single"]), n,
                                     "" if c["in_range"] else "← 超出 2800—3300"))

    data["master_sha256"] = sha(MASTER)
    data["revision"] = {
        "date": "2026-09-30",
        "note": "2026-09-30 对话修订闭环后的新基线（v1 保留为上一轮审稿记录，不覆盖）：单章切到新版本，合订稿为定点同步后的投递稿；"
                "combined_* 行号已失效，章节位置请用 sync_combined.py 的抬头定位。",
    }
    print("\n合计 %d 汉字；最少 %d、最多 %d" % (total, lo, hi))
    print("合订稿 sha256 %s" % data["master_sha256"][:16])
    if not args.apply:
        print("（未写入，加 --apply 才落盘）")
        return 0
    with open(BASELINE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("已写入 %s" % os.path.relpath(BASELINE, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
