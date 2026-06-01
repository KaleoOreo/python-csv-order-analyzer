import csv

INPUT_FILE = "data/orders.csv"
SUMMARY_FILE = "reports/summary.txt"
CLEAN_ORDERS_FILE = "reports/clean_orders.csv"
INVALID_ORDERS_FILE = "reports/invalid_orders.csv"
DUPLICATE_ORDERS_FILE = "reports/duplicate_orders.csv"

valid_orders = []
invalid_orders = []
duplicate_orders = []
seen_order_ids = set()

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        order_id = row["order_id"].strip()
        product = row["product"].strip()
        quantity_text = row["quantity"].strip()
        unit_price_text = row["unit_price"].strip()

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
        except ValueError:
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

total_revenue = 0
product_sales = {}

for order in valid_orders:
    total_revenue += order["revenue"]

    product = order["product"]
    revenue = order["revenue"]

    product_sales[product] = product_sales.get(product, 0) + revenue

best_product = max(product_sales, key=product_sales.get)
best_product_revenue = product_sales[best_product]

print()
print("Sales Data Quality Report")
print("-------------------------")
print(f"Valid orders: {len(valid_orders)}")
print(f"Invalid orders: {len(invalid_orders)}")
print(f"Duplicate orders: {len(duplicate_orders)}")
print(f"Total revenue: ${total_revenue:.2f}")
print(f"Best product: {best_product} (${best_product_revenue:.2f})")

print()
print("Revenue by Product")
print("------------------")

for product, revenue in product_sales.items():
    print(f"{product}: ${revenue:.2f}")

with open(SUMMARY_FILE, "w", encoding="utf-8") as file:
    file.write("Sales Data Quality Report\n")
    file.write("-------------------------\n")
    file.write(f"Valid orders: {len(valid_orders)}\n")
    file.write(f"Invalid orders: {len(invalid_orders)}\n")
    file.write(f"Duplicate orders: {len(duplicate_orders)}\n")
    file.write(f"Total revenue: ${total_revenue:.2f}\n")
    file.write(f"Best product: {best_product} (${best_product_revenue:.2f})\n")
    file.write("\nRevenue by Product\n")
    file.write("------------------\n")

    for product, revenue in product_sales.items():
        file.write(f"{product}: ${revenue:.2f}\n")

clean_fieldnames = [
    "order_id",
    "customer",
    "product",
    "quantity",
    "unit_price",
    "order_date",
    "revenue",
]

error_fieldnames = [
    "order_id",
    "customer",
    "product",
    "quantity",
    "unit_price",
    "order_date",
    "error",
]

with open(CLEAN_ORDERS_FILE, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=clean_fieldnames)
    writer.writeheader()
    writer.writerows(valid_orders)

with open(INVALID_ORDERS_FILE, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=error_fieldnames)
    writer.writeheader()
    writer.writerows(invalid_orders)

with open(DUPLICATE_ORDERS_FILE, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=error_fieldnames)
    writer.writeheader()
    writer.writerows(duplicate_orders)