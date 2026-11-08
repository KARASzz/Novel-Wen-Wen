#!/usr/bin/env python3
"""Report heuristic rhythm and cliché signals in Chinese web-novel prose."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CLICHES = [
    "仿佛", "宛如", "似乎", "缓缓", "微微", "轻轻", "嘴角勾起",
    "眼中闪过", "瞳孔骤缩", "倒吸一口凉气", "全场死寂",
    "空气仿佛凝固", "所有人都惊呆了", "然而", "与此同时",
    "下一秒", "就在这时", "这意味着", "显而易见", "他不知道的是",
    "命运的齿轮", "一场风暴即将来临",
]


def chinese_count(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def analyse(text: str) -> dict[str, object]:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    lengths = [chinese_count(p) for p in paragraphs]
    nonzero = [n for n in lengths if n]
    long_paragraphs = [
        {"index": i + 1, "chinese_chars": n}
        for i, n in enumerate(lengths)
        if n > 180
    ]
    one_sentence_runs = 0
    current_run = 0
    max_run = 0
    for p in paragraphs:
        sentences = len(re.findall(r"[。！？!?]", p))
        if sentences <= 1 and chinese_count(p) > 0:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    one_sentence_runs = max_run
    phrase_hits = {phrase: text.count(phrase) for phrase in CLICHES if text.count(phrase)}
    dialogue_paragraphs = sum(1 for p in paragraphs if "“" in p or '"' in p)
    total = chinese_count(text)
    return {
        "chinese_characters": total,
        "paragraphs": len(paragraphs),
        "average_chinese_chars_per_paragraph": round(sum(nonzero) / len(nonzero), 1) if nonzero else 0,
        "dialogue_paragraph_ratio": round(dialogue_paragraphs / len(paragraphs), 3) if paragraphs else 0,
        "long_paragraphs_over_180_chars": long_paragraphs,
        "max_consecutive_short_single_sentence_paragraphs": one_sentence_runs,
        "cliche_phrase_hits": phrase_hits,
        "notes": [
            "These are review signals, not automatic failures.",
            "Judge phrase hits in context; natural Chinese may legitimately use them.",
            "Hook, causality, payoff, character voice, and continuity require human review.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("path", nargs="?", help="UTF-8 text or Markdown chapter")
    group.add_argument("--text", help="Prose supplied directly on the command line")
    args = parser.parse_args()
    if args.text is not None:
        source = args.text
    else:
        source = Path(args.path).read_text(encoding="utf-8")
    print(json.dumps(analyse(source), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
