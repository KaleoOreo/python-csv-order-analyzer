import streamlit as st
import pandas as pd
from pathlib import Path

from src.processing import classify_orders
from src.summary import summarize_orders


st.set_page_config(page_title="CSV Order Analyzer", layout="wide")

st.title("CSV Order Analyzer — Interactive Demo")

st.markdown(
    """Upload an orders CSV or use the included sample dataset. The app will
validate rows, detect duplicates, compute revenue, and show summary charts."""
)

sample_path = Path("data/sample_orders.csv")

uploaded = st.sidebar.file_uploader("Upload CSV", type=["csv"])
use_sample = st.sidebar.checkbox("Use sample dataset", value=not uploaded)

if uploaded and not use_sample:
    df = pd.read_csv(uploaded)
else:
    df = pd.read_csv(sample_path)

rows = df.to_dict(orient="records")
valid, invalid, duplicates = classify_orders(rows)
summary = summarize_orders(valid, invalid, duplicates)

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Cleaned Orders")
    if valid:
        st.dataframe(pd.DataFrame(valid))
    else:
        st.write("No valid orders found.")

    st.subheader("Invalid / Duplicate Rows")
    if invalid or duplicates:
        st.dataframe(pd.DataFrame(invalid + duplicates))
    else:
        st.write("No invalid or duplicate rows.")

with col2:
    st.subheader("Summary")
    st.metric("Valid orders", len(valid))
    st.metric("Invalid orders", len(invalid))
    st.metric("Duplicate orders", len(duplicates))
    st.metric("Total revenue", f"${summary['total_revenue']:.2f}")
    st.metric("Average order", f"${summary['average_order_value']:.2f}")

st.subheader("Revenue by Product")
if summary["product_sales"]:
    prod_df = pd.DataFrame.from_dict(summary["product_sales"], orient="index", columns=["revenue"]).reset_index()
    prod_df.columns = ["product", "revenue"]
    st.bar_chart(prod_df.set_index("product"))
else:
    st.write("No product revenue to show.")

st.subheader("Revenue by Customer")
if summary["customer_sales"]:
    cust_df = pd.DataFrame.from_dict(summary["customer_sales"], orient="index", columns=["revenue"]).reset_index()
    cust_df.columns = ["customer", "revenue"]
    st.bar_chart(cust_df.set_index("customer"))
else:
    st.write("No customer revenue to show.")

st.markdown("---")
st.markdown("Run the CLI with: `python src/main.py --input path/to/orders.csv --reports-dir reports`")
