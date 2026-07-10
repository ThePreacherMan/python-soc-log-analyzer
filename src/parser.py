"""
parser.py

Responsible for loading and parsing authentication log files.
"""

import csv


def load_log_file(file_path):
    """
    Load authentication logs from a CSV file.

    Args:
        file_path: Path to the CSV authentication log file.

    Returns:
        list: Authentication events represented as dictionaries.
    """

    events = []

    with open(file_path, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            events.append(row)

    return events
