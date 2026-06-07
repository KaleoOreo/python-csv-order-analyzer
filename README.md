# CSV Order Analyzer

A small Python CLI project that cleans, validates, and summarizes order data stored in CSV files. This project is intended as a portfolio piece to demonstrate data cleaning, validation, reporting, testing, and CI for a CS application.

## Features

- Validate rows (missing fields, invalid numbers, non-positive values).
- Detect duplicate order IDs.
- Compute per-order revenue and aggregate statistics (total revenue, best product, best customer, average order value).
- Produce cleaned CSVs (`reports/clean_orders.csv`), invalid row CSVs, duplicate CSVs, and a human-readable summary (`reports/summary.txt`).

## Installation

Requires Python 3.10+.

Install dev/test deps:

```bash
python -m pip install -r requirements.txt
```

Build & install as a local package (creates an executable entry point):

```bash
python -m pip install -e .
# or: python -m pip install .
```

After installing, run the CLI using the generated script:

```bash
csv-order-analyzer --help
```

## Usage

Run the CLI (uses `data/orders.csv` and `reports/` by default):

```bash
python src/main.py
```

Specify custom input / output:

```bash
python src/main.py --input path/to/orders.csv --reports-dir path/to/reports
```

Output files (written to `reports/` by default):

- `summary.txt` — human-readable analytics report
- `clean_orders.csv` — validated orders with `revenue` added
- `invalid_orders.csv` — rows classified as invalid (contains `error` column)
- `duplicate_orders.csv` — rows classified as duplicates (contains `error` column)

## Testing

A lightweight test runner is included for environments without `pytest`:

```bash
python run_tests.py
```

If you have `pytest` installed:

```bash
python -m pytest -q
```

Interactive demo (Streamlit):

```bash
streamlit run streamlit_app.py
```

The Streamlit app provides a quick interactive view of cleaned orders and
visualizations, and accepts a CSV upload or the included `data/sample_orders.csv`.

## Development Notes

See `DEVELOPMENT_LOG.md` for a running log of changes and next steps.

## Contributing

Contributions welcome — open issues or submit PRs. Keep changes small and include tests.

## License

MIT License — see LICENSE (not included).
