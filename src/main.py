"""
python-soc-log-analyzer

Main application entry point.
"""

from pathlib import Path

from parser import load_log_file
from detector import detect_failed_logins
from report import generate_summary


BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "sample_logs" / "authentication_logs.csv"


def main():
    """
    Run the SOC Log Analyzer.
    """

    events = load_log_file(LOG_FILE)

    failed_logins = detect_failed_logins(events)

    total_events = len(events)

    generate_summary(total_events, failed_logins)


if __name__ == "__main__":
    main()
