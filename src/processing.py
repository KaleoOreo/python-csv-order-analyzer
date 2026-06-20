"""Order processing helpers.

This module contains functions to normalize and classify rows from a CSV
representing orders. It separates valid orders from invalid and duplicate
entries so the rest of the pipeline can operate on clean data.
"""

import math
from numbers import Real
from typing import List, Tuple, Dict, Any


def is_missing_value(value: Any) -> bool:
    """Return True for values that represent a blank CSV cell."""
    return value is None or (isinstance(value, Real) and math.isnan(value))


def normalize_row(row: Dict[str, Any]) -> Dict[str, str]:
    """Return a copy of ``row`` with all string fields stripped.

    Non-string values are coerced to strings before stripping.
    """
    return {
        field_name: "" if is_missing_value(field_value) else str(field_value).strip()
        for field_name, field_value in row.items()
    }


def classify_orders(rows: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Validate and classify order rows.

    Args:
        rows: A list of dict-like rows (as returned by ``csv.DictReader``).

    Returns:
        A tuple of three lists: (valid_orders, invalid_orders, duplicate_orders).
        Valid orders will include computed numeric fields (`quantity`,
        `unit_price`, `revenue`). Invalid and duplicate rows will include an
        `error` field describing the problem.
    """
    valid_orders: List[Dict[str, Any]] = []
    invalid_orders: List[Dict[str, Any]] = []
    duplicate_orders: List[Dict[str, Any]] = []
    seen_order_ids = set()

    for original_row in rows:
        row = normalize_row(original_row)
        order_id = row.get("order_id", "")
        product = row.get("product", "")
        quantity_text = row.get("quantity", "")
        unit_price_text = row.get("unit_price", "")

        if order_id == "":
            row["error"] = "Missing order ID"
            invalid_orders.append(row)
            continue

        if order_id in seen_order_ids:
            row["error"] = "Duplicate order ID"
            duplicate_orders.append(row)
            continue

        if product == "":
            row["error"] = "Missing product"
            invalid_orders.append(row)
            continue

        try:
            quantity = int(quantity_text)
            unit_price = float(unit_price_text)
        except (ValueError, TypeError):
            row["error"] = "Invalid quantity or unit price"
            invalid_orders.append(row)
            continue

        if quantity <= 0:
            row["error"] = "Quantity must be positive"
            invalid_orders.append(row)
            continue

        if unit_price <= 0:
            row["error"] = "Unit price must be positive"
            invalid_orders.append(row)
            continue

        seen_order_ids.add(order_id)

        row["quantity"] = quantity
        row["unit_price"] = unit_price
        row["revenue"] = quantity * unit_price

        valid_orders.append(row)

    return valid_orders, invalid_orders, duplicate_orders
