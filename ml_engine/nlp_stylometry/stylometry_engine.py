import numpy as np
from typing import Dict


class StylometryEngine:
    """
    Computes writing-style similarity between two accounts.
    """

    def cosine_similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        if a is None or b is None:
            return 0.0
        if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
            return 0.0
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

    def compare(self, a: Dict, b: Dict) -> Dict:
        """
        a, b = {
            "punctuation": np.ndarray,
            "tfidf": np.ndarray,
            "syntax": np.ndarray,
            "semantic": np.ndarray,
            "uniqueness": float
        }
        """
        punctuation_sim = self.cosine_similarity(
            a["punctuation"], b["punctuation"]
        )
        vocab_sim = self.cosine_similarity(
            a["tfidf"], b["tfidf"]
        )
        syntax_sim = self.cosine_similarity(
            a["syntax"], b["syntax"]
        )
        semantic_sim = self.cosine_similarity(
            a["semantic"], b["semantic"]
        )

        uniqueness_sim = 1 - abs(
            a["uniqueness"] - b["uniqueness"]
        )

        stylometry_score = round(
            0.20 * punctuation_sim +
            0.25 * vocab_sim +
            0.20 * syntax_sim +
            0.25 * semantic_sim +
            0.10 * uniqueness_sim,
            4
        )

        return {
            "punctuation_similarity": round(punctuation_sim, 4),
            "vocab_similarity": round(vocab_sim, 4),
            "syntax_similarity": round(syntax_sim, 4),
            "semantic_similarity": round(semantic_sim, 4),
            "uniqueness_similarity": round(uniqueness_sim, 4),
            "stylometry_score": stylometry_score,
        }
