"""CLI entry point for the CSV Order Analyzer project.

This file wires together the processing, summarization, and I/O modules and
exposes a small command-line interface for running the pipeline against a
CSV file.
"""

import argparse
from pathlib import Path
from typing import List

from src.processing import classify_orders
from src.summary import summarize_orders, format_report
from src.io import write_csv_report, OUTPUT_FIELDNAMES


DEFAULT_INPUT_FILE = Path("data/orders.csv")
DEFAULT_REPORTS_DIR = Path("reports")

SUMMARY_FILE_NAME = "summary.txt"
CLEAN_ORDERS_FILE_NAME = "clean_orders.csv"
INVALID_ORDERS_FILE_NAME = "invalid_orders.csv"
DUPLICATE_ORDERS_FILE_NAME = "duplicate_orders.csv"

ERROR_FIELDNAMES: List[str] = OUTPUT_FIELDNAMES + ["error"]
CLEAN_FIELDNAMES: List[str] = OUTPUT_FIELDNAMES + ["revenue"]


def parse_arguments() -> argparse.Namespace:
    """Parse CLI arguments and return the result.

    Returns an argparse.Namespace with `.input` and `.reports_dir` attributes.
    """
    parser = argparse.ArgumentParser(
        description="Clean an orders CSV file and generate a small analytics report."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_FILE, help="Path to the raw orders CSV file.")
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=DEFAULT_REPORTS_DIR,
        help="Directory where cleaned files and reports should be written.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the full processing pipeline and write reports to disk."""
    arguments = parse_arguments()
    reports_dir = arguments.reports_dir
    reports_dir.mkdir(parents=True, exist_ok=True)

    with arguments.input.open("r", encoding="utf-8", newline="") as file:
        import csv

        reader = csv.DictReader(file)
        rows = list(reader)

    valid_orders, invalid_orders, duplicate_orders = classify_orders(rows)
    summary = summarize_orders(valid_orders, invalid_orders, duplicate_orders)
    report_text = format_report(summary)

    print()
    print(report_text, end="")

    (reports_dir / SUMMARY_FILE_NAME).write_text(report_text, encoding="utf-8")
    write_csv_report(reports_dir / CLEAN_ORDERS_FILE_NAME, CLEAN_FIELDNAMES, valid_orders)
    write_csv_report(reports_dir / INVALID_ORDERS_FILE_NAME, ERROR_FIELDNAMES, invalid_orders)
    write_csv_report(reports_dir / DUPLICATE_ORDERS_FILE_NAME, ERROR_FIELDNAMES, duplicate_orders)


if __name__ == "__main__":
    main()