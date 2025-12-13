import numpy as np
from typing import Dict


class BehaviorEngine:
    """
    Computes similarity between two accounts' behavior profiles.
    """

    def cosine_similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        if a is None or b is None:
            return 0.0
        if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
            return 0.0
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

    def compare(self, profile_a: Dict, profile_b: Dict) -> Dict:
        """
        profile = {
            "hourly_vector": np.ndarray(24),
            "weekday_vector": np.ndarray(7),
            "burstiness": float,
            "session_start_vector": np.ndarray(24),
            "avg_session_length": float,
            "rapid_sequence_freq": float
        }
        """
        hourly_sim = self.cosine_similarity(
            profile_a["hourly_vector"],
            profile_b["hourly_vector"]
        )

        weekday_sim = self.cosine_similarity(
            profile_a["weekday_vector"],
            profile_b["weekday_vector"]
        )

        session_start_sim = self.cosine_similarity(
            profile_a["session_start_vector"],
            profile_b["session_start_vector"]
        )

        burstiness_diff = 1 - abs(
            profile_a["burstiness"] - profile_b["burstiness"]
        )

        session_length_diff = 1 - abs(
            profile_a["avg_session_length"] - profile_b["avg_session_length"]
        ) / max(profile_a["avg_session_length"], profile_b["avg_session_length"], 1)

        rapid_seq_diff = 1 - abs(
            profile_a["rapid_sequence_freq"] - profile_b["rapid_sequence_freq"]
        )

        behavior_score = round(
            0.25 * hourly_sim +
            0.20 * weekday_sim +
            0.20 * session_start_sim +
            0.15 * burstiness_diff +
            0.10 * session_length_diff +
            0.10 * rapid_seq_diff,
            4
        )

        return {
            "hourly_similarity": round(hourly_sim, 4),
            "weekday_similarity": round(weekday_sim, 4),
            "session_start_similarity": round(session_start_sim, 4),
            "burstiness_similarity": round(burstiness_diff, 4),
            "session_length_similarity": round(session_length_diff, 4),
            "rapid_sequence_similarity": round(rapid_seq_diff, 4),
            "behavior_score": behavior_score,
        }
