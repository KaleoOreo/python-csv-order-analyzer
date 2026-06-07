"""Reporting helpers for orders analysis.

This module builds summaries and converts them to a human-readable report
string. Keeping reporting logic separate makes it easier to test and evolve
presentation without changing processing logic.
"""

from collections import Counter
from typing import List, Dict, Any


def summarize_orders(valid_orders: List[Dict[str, Any]], invalid_orders: List[Dict[str, Any]], duplicate_orders: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Compute summary statistics from validated orders.

    Returns a dictionary containing total and per-product/customer revenues,
    best product/customer, average order value, and error breakdowns.
    """
    total_revenue = 0.0
    product_sales: Dict[str, float] = {}
    customer_sales: Dict[str, float] = {}

    for order in valid_orders:
        revenue = float(order["revenue"])
        product = str(order["product"])
        customer = str(order.get("customer", ""))

        total_revenue += revenue
        product_sales[product] = product_sales.get(product, 0.0) + revenue
        customer_sales[customer] = customer_sales.get(customer, 0.0) + revenue

    best_product = max(product_sales, key=product_sales.get) if product_sales else "N/A"
    best_product_revenue = product_sales.get(best_product, 0.0)
    best_customer = max(customer_sales, key=customer_sales.get) if customer_sales else "N/A"
    best_customer_revenue = customer_sales.get(best_customer, 0.0)
    average_order_value = total_revenue / len(valid_orders) if valid_orders else 0.0

    invalid_reason_counts = Counter(row["error"] for row in invalid_orders + duplicate_orders)

    return {
        "valid_orders": valid_orders,
        "invalid_orders": invalid_orders,
        "duplicate_orders": duplicate_orders,
        "total_revenue": total_revenue,
        "product_sales": product_sales,
        "customer_sales": customer_sales,
        "best_product": best_product,
        "best_product_revenue": best_product_revenue,
        "best_customer": best_customer,
        "best_customer_revenue": best_customer_revenue,
        "average_order_value": average_order_value,
        "invalid_reason_counts": invalid_reason_counts,
    }


def format_report(summary: Dict[str, Any]) -> str:
    """Return a human-readable multi-line report for ``summary``.

    The result is suitable for printing to the console and writing to a
    plain text file.
    """
    lines = [
        "Sales Data Quality Report",
        "-------------------------",
        f"Valid orders: {len(summary['valid_orders'])}",
        f"Invalid orders: {len(summary['invalid_orders'])}",
        f"Duplicate orders: {len(summary['duplicate_orders'])}",
        f"Total revenue: ${summary['total_revenue']:.2f}",
        f"Average order value: ${summary['average_order_value']:.2f}",
        f"Best product: {summary['best_product']} (${summary['best_product_revenue']:.2f})",
        f"Best customer: {summary['best_customer']} (${summary['best_customer_revenue']:.2f})",
        "",
        "Revenue by Product",
        "------------------",
    ]

    for product, revenue in sorted(summary["product_sales"].items(), key=lambda item: item[1], reverse=True):
        lines.append(f"{product}: ${revenue:.2f}")

    lines.extend([
        "",
        "Revenue by Customer",
        "-------------------",
    ])

    for customer, revenue in sorted(summary["customer_sales"].items(), key=lambda item: item[1], reverse=True):
        lines.append(f"{customer}: ${revenue:.2f}")

    lines.extend([
        "",
        "Error Breakdown",
        "---------------",
    ])

    for error_message, count in sorted(summary["invalid_reason_counts"].items(), key=lambda item: item[1], reverse=True):
        lines.append(f"{error_message}: {count}")

    return "\n".join(lines) + "\n"
