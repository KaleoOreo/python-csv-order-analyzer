"""I/O helpers for writing CSV and report files.

Keeping these separate makes the main script easier to test and allows
replacing file writing with other sinks (e.g. S3, database) later.
"""

import csv
from pathlib import Path
from typing import List, Dict, Any


OUTPUT_FIELDNAMES: List[str] = [
    "order_id",
    "customer",
    "product",
    "quantity",
    "unit_price",
    "order_date",
]


def write_csv_report(file_path: Path, fieldnames: List[str], rows: List[Dict[str, Any]]) -> None:
    """Write a list of dictionaries to ``file_path`` as a CSV.

    Args:
        file_path: Destination path to write.
        fieldnames: Column order for the CSV header.
        rows: Iterable of mapping objects (dictionaries) for each row.
    """
    with file_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
