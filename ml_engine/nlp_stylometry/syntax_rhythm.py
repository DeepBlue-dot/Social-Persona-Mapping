import numpy as np
import re
from typing import List


class SyntaxRhythm:
    """
    Analyzes syntactic rhythm and formatting habits.
    """

    def sentence_lengths(self, texts: List[str]) -> np.ndarray:
        lengths = []
        for text in texts:
            sentences = re.split(r"[.!?]", text)
            lengths.extend([len(s.split()) for s in sentences if s.strip()])
        return np.array(lengths)

    def capitalization_ratio(self, texts: List[str]) -> float:
        total = sum(len(t) for t in texts)
        if total == 0:
            return 0.0
        caps = sum(sum(1 for c in t if c.isupper()) for t in texts)
        return caps / total

    def emoji_frequency(self, texts: List[str]) -> float:
        emoji_pattern = re.compile(
            "[\U0001F600-\U0001F64F"
            "\U0001F300-\U0001F5FF"
            "\U0001F680-\U0001F6FF"
            "\U0001F1E0-\U0001F1FF]+",
            flags=re.UNICODE,
        )
        emojis = sum(len(emoji_pattern.findall(t)) for t in texts)
        total_words = sum(len(t.split()) for t in texts)
        return emojis / total_words if total_words > 0 else 0.0

    def build_profile(self, texts: List[str]) -> np.ndarray:
        lengths = self.sentence_lengths(texts)

        return np.array([
            lengths.mean() if len(lengths) else 0.0,
            lengths.var() if len(lengths) else 0.0,
            self.capitalization_ratio(texts),
            self.emoji_frequency(texts),
        ])
