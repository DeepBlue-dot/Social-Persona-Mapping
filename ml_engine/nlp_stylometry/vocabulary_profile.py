import numpy as np
from collections import Counter
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer


class VocabularyProfile:
    """
    Extracts vocabulary usage patterns.
    """

    def __init__(self, top_n: int = 50):
        self.top_n = top_n
        self.vectorizer = TfidfVectorizer(
            max_features=300,
            ngram_range=(1, 2),
            stop_words="english"
        )

    def top_words(self, texts: List[str]) -> np.ndarray:
        tokens = " ".join(texts).lower().split()
        counts = Counter(tokens)
        most_common = counts.most_common(self.top_n)
        return np.array([freq for _, freq in most_common])

    def uniqueness_score(self, texts: List[str]) -> float:
        tokens = " ".join(texts).split()
        if not tokens:
            return 0.0
        return len(set(tokens)) / len(tokens)

    def tfidf_signature(self, texts: List[str]) -> np.ndarray:
        tfidf = self.vectorizer.fit_transform(texts)
        return tfidf.mean(axis=0).A1

    def build_profile(self, texts: List[str]) -> dict:
        return {
            "top_words": self.top_words(texts),
            "uniqueness": self.uniqueness_score(texts),
            "tfidf": self.tfidf_signature(texts),
        }
