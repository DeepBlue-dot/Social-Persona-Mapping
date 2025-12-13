from typing import Dict

class AccountLinkingEngine:
    """
    Combines multiple similarity signals to determine whether
    two accounts belong to the same individual.
    """

    def __init__(
        self,
        username_weight: float = 0.25,
        image_weight: float = 0.25,
        stylometry_weight: float = 0.20,
        behavior_weight: float = 0.15,
        topic_weight: float = 0.15,
    ):
        self.weights = {
            "username": username_weight,
            "image": image_weight,
            "stylometry": stylometry_weight,
            "behavior": behavior_weight,
            "topics": topic_weight,
        }

    def compute_score(self, scores: Dict[str, float]) -> float:
        """
        Combine weighted scores into a final similarity score.
        All input scores must be normalized (0–1).
        """
        final_score = 0.0
        for key, weight in self.weights.items():
            final_score += weight * scores.get(key, 0.0)
        return round(final_score, 4)

    def confidence_level(self, score: float) -> str:
        if score >= 0.80:
            return "High"
        elif score >= 0.50:
            return "Medium"
        return "Low"

    def link_accounts(self, score_breakdown: Dict[str, float]) -> Dict:
        """
        Main entry point.
        """
        score = self.compute_score(score_breakdown)
        confidence = self.confidence_level(score)

        return {
            "final_score": score,
            "confidence": confidence,
            "breakdown": score_breakdown,
        }
