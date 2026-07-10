"""
python-soc-log-analyzer

Main application entry point.
"""

from parser import load_log_file
from detector import detect_failed_logins
from report import generate_summary


def main():
    """
    Run the SOC Log Analyzer.
    """

    file_path = "../sample_logs/authentication_logs.csv"

    events = load_log_file(file_path)

    failed_logins = detect_failed_logins(events)

    total_events = len(events)

    generate_summary(total_events, failed_logins)


if __name__ == "__main__":
    main()
