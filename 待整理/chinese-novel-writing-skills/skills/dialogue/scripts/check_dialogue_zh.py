#!/usr/bin/env python3
"""Report heuristic voice and dialogue risks in Chinese fiction."""

from __future__ import annotations

import argparse
import json
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path


TEMPLATE_PHRASES = [
    "你也知道", "我明白你的意思", "请你相信我", "你要明白",
    "这意味着", "无论如何", "总而言之", "说实话",
    "声音不大，却", "不容置疑", "淡淡地说", "冷冷地说",
    "嘴角微微上扬", "深吸一口气", "攥紧拳头",
]

SPEAKER_LINE = re.compile(r"^\s*([\u4e00-\u9fffA-Za-z0-9_·]{1,16})[：:]\s*(.+)$")
QUOTED = re.compile(r"[“\"]([^”\"]+)[”\"]")


def chinese_count(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def cv(values: list[int]) -> float | None:
    usable = [value for value in values if value > 0]
    if len(usable) < 2 or statistics.mean(usable) == 0:
        return None
    return round(statistics.pstdev(usable) / statistics.mean(usable), 3)


def extract_dialogue(text: str) -> tuple[list[str], dict[str, list[str]]]:
    lines: list[str] = []
    by_speaker: dict[str, list[str]] = defaultdict(list)
    for raw_line in text.splitlines():
        match = SPEAKER_LINE.match(raw_line)
        if match:
            speaker, utterance = match.groups()
            utterance = utterance.strip("“”\" ")
            if utterance:
                lines.append(utterance)
                by_speaker[speaker].append(utterance)
            continue
        for utterance in QUOTED.findall(raw_line):
            utterance = utterance.strip()
            if utterance:
                lines.append(utterance)
    return lines, dict(by_speaker)


def analyse(text: str) -> dict[str, object]:
    lines, by_speaker = extract_dialogue(text)
    lengths = [chinese_count(line) for line in lines]
    phrase_hits = {phrase: text.count(phrase) for phrase in TEMPLATE_PHRASES if text.count(phrase)}

    openings = Counter()
    for line in lines:
        opening = re.sub(r"^[，。！？!?…—\s]+", "", line)[:4]
        if len(opening) >= 2:
            openings[opening] += 1

    speaker_stats = {}
    for speaker, utterances in by_speaker.items():
        speaker_lengths = [chinese_count(line) for line in utterances]
        questions = sum(1 for line in utterances if "？" in line or "?" in line)
        speaker_stats[speaker] = {
            "lines": len(utterances),
            "average_chinese_chars": round(sum(speaker_lengths) / len(speaker_lengths), 1),
            "question_ratio": round(questions / len(utterances), 3),
        }

    exposition_candidates = [
        index + 1
        for index, line in enumerate(lines)
        if chinese_count(line) >= 55 or re.search(r"(?:首先|其次|最后|原因是|这意味着|你也知道)", line)
    ]
    uniformity_note = None
    length_cv = cv(lengths)
    if length_cv is not None and len(lines) >= 6 and length_cv < 0.28:
        uniformity_note = "Dialogue line lengths are unusually uniform; review rhythm in context."

    return {
        "dialogue_lines": len(lines),
        "average_chinese_chars_per_line": round(sum(lengths) / len(lengths), 1) if lengths else 0,
        "dialogue_length_cv": length_cv,
        "uniformity_note": uniformity_note,
        "speaker_stats_for_labeled_lines": speaker_stats,
        "repeated_openings": {key: count for key, count in openings.items() if count >= 3},
        "template_phrase_hits": phrase_hits,
        "exposition_candidate_line_numbers": exposition_candidates,
        "notes": [
            "Signals are review candidates, not automatic failures.",
            "Speaker statistics require lines formatted as Name: dialogue or Name：dialogue.",
            "Subtext, power shifts, factual accuracy, and character fit require human review.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("path", nargs="?", help="UTF-8 text or Markdown scene")
    source.add_argument("--text", help="Dialogue supplied directly")
    args = parser.parse_args()
    text = args.text if args.text is not None else Path(args.path).read_text(encoding="utf-8")
    print(json.dumps(analyse(text), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
