"""
report.py

Responsible for generating the security report.
"""


def generate_summary(total_events, failed_logins):
    """
    Generate a simple security summary.

    Args:
        total_events (int): Total authentication events.
        failed_logins (int): Total failed login attempts.
    """

    print("\n========== SECURITY SUMMARY ==========")
    print(f"Total Events      : {total_events}")
    print(f"Failed Logins     : {failed_logins}")
    print("======================================")
