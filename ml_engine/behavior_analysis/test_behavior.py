from datetime import datetime, timedelta
import random

from timestamp_profile import TimestampProfile
from session_detector import SessionDetector
from behavior_engine import BehaviorEngine


def generate_fake_timestamps(
    days=14,
    posts_per_day=10,
    active_hours=(9, 22)
):
    """
    Simulate realistic posting behavior
    """
    timestamps = []
    now = datetime.now()

    for d in range(days):
        day = now - timedelta(days=d)
        for _ in range(posts_per_day):
            hour = random.randint(*active_hours)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            timestamps.append(
                day.replace(hour=hour, minute=minute, second=second)
            )

    return sorted(timestamps)


def build_behavior_profile(timestamps):
    tp = TimestampProfile()
    sd = SessionDetector()

    ts_profile = tp.build_profile(timestamps)
    session_profile = sd.build_profile(timestamps)

    return {
        **ts_profile,
        **session_profile
    }


if __name__ == "__main__":
    print("\n=== Generating fake user behavior ===")

    # User A: morning + afternoon activity
    user_a_timestamps = generate_fake_timestamps(
        active_hours=(8, 16)
    )

    # User B: afternoon + evening activity
    user_b_timestamps = generate_fake_timestamps(
        active_hours=(12, 22)
    )

    profile_a = build_behavior_profile(user_a_timestamps)
    profile_b = build_behavior_profile(user_b_timestamps)

    engine = BehaviorEngine()
    result = engine.compare(profile_a, profile_b)

    print("\n=== Behavior Comparison Result ===")
    for k, v in result.items():
        print(f"{k}: {v}")
