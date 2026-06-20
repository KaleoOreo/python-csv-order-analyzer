from src.processing import classify_orders
from src.summary import summarize_orders


def test_classify_orders_mixed_cases():
    rows = [
        {"order_id": "1001", "customer": "Amy", "product": "Li Hing Plum", "quantity": "2", "unit_price": "28.25", "order_date": "2026-05-01"},
        {"order_id": "1002", "customer": "Ben", "product": "", "quantity": "1", "unit_price": "2.02", "order_date": "2026-05-01"},
        {"order_id": "1001", "customer": "Amy", "product": "Li Hing Plum", "quantity": "2", "unit_price": "28.25", "order_date": "2026-05-01"},
        {"order_id": "1003", "customer": "Chris", "product": "Nibb-its", "quantity": "0", "unit_price": "2.02", "order_date": "2026-05-02"},
        {"order_id": "1004", "customer": "Dana", "product": "Nibb-its", "quantity": "3", "unit_price": "bad", "order_date": "2026-05-03"},
    ]

    valid, invalid, duplicates = classify_orders(rows)

    assert len(valid) == 1
    assert len(invalid) == 3
    assert len(duplicates) == 1

    v = valid[0]
    assert v["order_id"] == "1001"
    assert v["quantity"] == 2
    assert abs(v["unit_price"] - 28.25) < 1e-6
    assert abs(v["revenue"] - 56.5) < 1e-6


def test_classify_orders_treats_nan_like_blank_cells():
    rows = [
        {"order_id": "2001", "customer": "Amy", "product": float("nan"), "quantity": "2", "unit_price": "28.25", "order_date": "2026-05-01"},
        {"order_id": "2002", "customer": "Ben", "product": "Nibb-its", "quantity": "1", "unit_price": float("nan"), "order_date": "2026-05-01"},
    ]

    valid, invalid, duplicates = classify_orders(rows)

    assert valid == []
    assert duplicates == []
    assert len(invalid) == 2
    assert invalid[0]["error"] == "Missing product"
    assert invalid[1]["error"] == "Invalid quantity or unit price"


def test_summarize_orders_basic():
    valid_orders = [
        {"order_id": "1001", "customer": "Amy", "product": "P", "quantity": 2, "unit_price": 10.0, "revenue": 20.0},
        {"order_id": "1005", "customer": "Ben", "product": "Q", "quantity": 1, "unit_price": 5.0, "revenue": 5.0},
    ]

    summary = summarize_orders(valid_orders, [], [])

    assert abs(summary["total_revenue"] - 25.0) < 1e-6
    assert summary["best_product"] == "P"
    assert abs(summary["best_product_revenue"] - 20.0) < 1e-6
    assert summary["best_customer"] == "Amy"
    assert abs(summary["average_order_value"] - 12.5) < 1e-6
