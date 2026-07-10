"""
report.py

Responsible for generating security reports.
"""


def generate_summary(total_events, failed_logins, alerts):
    """
    Display the authentication security summary.

    Args:
        total_events (int): Total authentication events.
        failed_logins (int): Total failed login attempts.
        alerts (list): Detected brute-force alerts.
    """

    successful_logins = total_events - failed_logins

    print("\n========== SECURITY SUMMARY ==========")
    print(f"Total Events       : {total_events}")
    print(f"Successful Logins  : {successful_logins}")
    print(f"Failed Logins      : {failed_logins}")
    print(f"Security Alerts    : {len(alerts)}")
    print("======================================")

    if alerts:
        print("\n========== HIGH-RISK ALERTS ==========")

        for alert_number, alert in enumerate(alerts, start=1):
            print(f"\nAlert #{alert_number}")
            print(f"User               : {alert['user']}")
            print(f"IP Address         : {alert['ip_address']}")
            print(f"Failed Attempts    : {alert['failed_attempts']}")
            print(f"Risk Level         : {alert['risk_level']}")
            print(f"Reason             : {alert['reason']}")

        print("\n======================================")
    else:
        print("\nNo brute-force activity detected.")
