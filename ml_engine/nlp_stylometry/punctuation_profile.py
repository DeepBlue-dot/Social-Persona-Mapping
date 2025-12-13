import re
import numpy as np
from typing import List


class PunctuationProfile:
    """
    Extracts punctuation usage patterns from text.
    """

    PUNCTUATION = [",", ".", "?", "!", "...", ";", ":"]

    def extract(self, texts: List[str]) -> np.ndarray:
        counts = np.zeros(len(self.PUNCTUATION) + 3)

        for text in texts:
            for i, p in enumerate(self.PUNCTUATION):
                counts[i] += text.count(p)

            # Repeated punctuation (!!!, ???)
            counts[-3] += len(re.findall(r"[!?]{2,}", text))

            # Special symbols
            counts[-2] += len(re.findall(r"[@#$%^&*]", text))

            # Repeated characters (loooool)
            counts[-1] += len(re.findall(r"(.)\1{2,}", text))

        return self._normalize(counts)

    def _normalize(self, vec: np.ndarray) -> np.ndarray:
        total = vec.sum()
        return vec / total if total > 0 else vec
