import numpy as np
from datetime import datetime
from typing import List


class TimestampProfile:
    """
    Generates timestamp-based behavioral vectors.
    """

    def __init__(self):
        self.HOURS = 24
        self.DAYS = 7

    def hour_of_day_histogram(self, timestamps: List[datetime]) -> np.ndarray:
        vec = np.zeros(self.HOURS)
        for ts in timestamps:
            vec[ts.hour] += 1
        return self._normalize(vec)

    def weekday_histogram(self, timestamps: List[datetime]) -> np.ndarray:
        vec = np.zeros(self.DAYS)
        for ts in timestamps:
            vec[ts.weekday()] += 1
        return self._normalize(vec)

    def posting_burstiness(self, timestamps: List[datetime]) -> float:
        """
        Measures burstiness using inter-post time variance.
        """
        if len(timestamps) < 2:
            return 0.0

        timestamps = sorted(timestamps)
        deltas = [
            (timestamps[i + 1] - timestamps[i]).total_seconds()
            for i in range(len(timestamps) - 1)
        ]

        mean = np.mean(deltas)
        std = np.std(deltas)
        if mean == 0:
            return 0.0

        return round(std / mean, 4)

    def build_profile(self, timestamps: List[datetime]) -> dict:
        return {
            "hourly_vector": self.hour_of_day_histogram(timestamps),
            "weekday_vector": self.weekday_histogram(timestamps),
            "burstiness": self.posting_burstiness(timestamps),
        }

    def _normalize(self, vec: np.ndarray) -> np.ndarray:
        total = vec.sum()
        return vec / total if total > 0 else vec
