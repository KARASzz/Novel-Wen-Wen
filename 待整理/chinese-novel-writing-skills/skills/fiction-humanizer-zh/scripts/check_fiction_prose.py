#!/usr/bin/env python3
"""Report review signals in Chinese fiction without assigning an AI score."""

from __future__ import annotations

import argparse
import json
import re
import statistics
from collections import Counter
from pathlib import Path


PHRASE_GROUPS = {
    "模糊滤镜": ["仿佛", "宛如", "似乎", "好像"],
    "机械微动作": ["缓缓", "微微", "轻轻", "嘴角上扬", "嘴角勾起", "眼中闪过", "瞳孔骤缩", "攥紧拳头", "深吸一口气"],
    "群体反应": ["倒吸一口凉气", "全场死寂", "所有人都惊呆了", "不敢置信"],
    "万能转场": ["然而", "与此同时", "下一秒", "就在这时"],
    "解释总结": ["这意味着", "显而易见", "之所以", "总而言之", "可见"],
    "空泛章末": ["一切才刚刚开始", "才刚刚开始", "命运的齿轮", "一场风暴即将来临", "他不知道的是"],
}

PATTERNS = {
    "否定式反转": re.compile(r"不是.{0,28}(?:而是|只是)"),
    "否定式对称": re.compile(r"没有.{0,28}(?:只有|只剩)"),
    "因果解释": re.compile(r"之所以.{0,45}是因为"),
    "抽象情绪容器": re.compile(r"(?:一种|一股|一阵).{0,18}(?:情绪|感觉|孤独|愤怒|悲伤|恐惧|暖意|寒意)"),
}


def chinese_count(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def coefficient_of_variation(values: list[int]) -> float | None:
    usable = [value for value in values if value > 0]
    if len(usable) < 2 or statistics.mean(usable) == 0:
        return None
    return round(statistics.pstdev(usable) / statistics.mean(usable), 3)


def analyse(text: str) -> dict[str, object]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    paragraph_lengths = [chinese_count(part) for part in paragraphs]
    sentences = [part.strip() for part in re.split(r"[。！？!?]+", text) if chinese_count(part)]
    sentence_lengths = [chinese_count(part) for part in sentences]

    phrase_hits: dict[str, dict[str, int]] = {}
    repeated_phrases: dict[str, int] = {}
    for group, phrases in PHRASE_GROUPS.items():
        hits = {phrase: text.count(phrase) for phrase in phrases if text.count(phrase)}
        if hits:
            phrase_hits[group] = hits
            repeated_phrases.update({phrase: count for phrase, count in hits.items() if count >= 2})

    pattern_hits = {
        name: len(pattern.findall(text))
        for name, pattern in PATTERNS.items()
        if pattern.search(text)
    }

    short_run = 0
    max_short_run = 0
    for part, length in zip(paragraphs, paragraph_lengths):
        sentence_count = len(re.findall(r"[。！？!?]", part))
        if 0 < length <= 45 and sentence_count <= 1:
            short_run += 1
            max_short_run = max(max_short_run, short_run)
        else:
            short_run = 0

    final_window = text[-300:]
    ending_hits = [phrase for phrase in PHRASE_GROUPS["空泛章末"] if phrase in final_window]
    long_paragraphs = [index + 1 for index, length in enumerate(paragraph_lengths) if length > 220]
    category_counts = Counter({group: sum(hits.values()) for group, hits in phrase_hits.items()})

    return {
        "chinese_characters": chinese_count(text),
        "paragraphs": len(paragraphs),
        "paragraph_length_cv": coefficient_of_variation(paragraph_lengths),
        "sentence_length_cv": coefficient_of_variation(sentence_lengths),
        "long_paragraph_indices_over_220_chars": long_paragraphs,
        "max_consecutive_short_single_sentence_paragraphs": max_short_run,
        "phrase_hits_by_group": phrase_hits,
        "repeated_phrase_candidates": repeated_phrases,
        "structural_pattern_hits": pattern_hits,
        "ending_cliche_hits_in_last_300_chars": ending_hits,
        "signal_groups_present": list(category_counts),
        "notes": [
            "These are review candidates, not proof of AI authorship.",
            "Modify only clustered signals that harm voice, clarity, causality, or rhythm.",
            "Quotes, names, intentional repetition, genre conventions, and author samples need contextual protection.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("path", nargs="?", help="UTF-8 text or Markdown chapter")
    source.add_argument("--text", help="Prose supplied directly on the command line")
    args = parser.parse_args()
    text = args.text if args.text is not None else Path(args.path).read_text(encoding="utf-8")
    print(json.dumps(analyse(text), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
