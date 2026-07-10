"""
detector.py

Responsible for detecting suspicious authentication activity.
"""


def detect_failed_logins(events):
    """
    Count failed login attempts.

    Args:
        events (list): Authentication log events.

    Returns:
        int: Number of failed login attempts.
    """

    failed_attempts = 0

    for event in events:
        if event["status"].upper() == "FAILED":
            failed_attempts += 1

    return failed_attempts
