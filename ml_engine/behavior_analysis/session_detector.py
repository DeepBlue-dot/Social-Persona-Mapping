from datetime import datetime
from typing import List
import numpy as np


class SessionDetector:
    """
    Detects user activity sessions from timestamps.
    """

    def __init__(self, session_gap_minutes: int = 30):
        self.session_gap = session_gap_minutes * 60  # seconds

    def detect_sessions(self, timestamps: List[datetime]) -> List[List[datetime]]:
        if not timestamps:
            return []

        timestamps = sorted(timestamps)
        sessions = [[timestamps[0]]]

        for prev, curr in zip(timestamps[:-1], timestamps[1:]):
            gap = (curr - prev).total_seconds()
            if gap <= self.session_gap:
                sessions[-1].append(curr)
            else:
                sessions.append([curr])

        return sessions

    def average_session_length(self, sessions: List[List[datetime]]) -> float:
        if not sessions:
            return 0.0

        durations = [
            (s[-1] - s[0]).total_seconds() / 60
            for s in sessions if len(s) > 1
        ]

        return round(np.mean(durations), 4) if durations else 0.0

    def session_start_times(self, sessions: List[List[datetime]]) -> np.ndarray:
        vec = np.zeros(24)
        for s in sessions:
            vec[s[0].hour] += 1
        return vec / vec.sum() if vec.sum() > 0 else vec

    def rapid_sequence_frequency(self, sessions: List[List[datetime]]) -> float:
        """
        Percentage of sessions with rapid posting behavior.
        """
        if not sessions:
            return 0.0

        rapid = sum(1 for s in sessions if len(s) >= 5)
        return round(rapid / len(sessions), 4)

    def build_profile(self, timestamps: List[datetime]) -> dict:
        sessions = self.detect_sessions(timestamps)
        return {
            "avg_session_length": self.average_session_length(sessions),
            "session_start_vector": self.session_start_times(sessions),
            "rapid_sequence_freq": self.rapid_sequence_frequency(sessions),
        }
