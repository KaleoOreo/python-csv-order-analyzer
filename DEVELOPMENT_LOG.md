# Development Log

This file records actions taken while building the CSV Order Analyzer project.

## 2026-06-07
- Initialized project workspace and inspected existing files.
- Refactored `src/main.py` into functions with CLI arguments and richer reporting.
- Added `src/__init__.py` to make `src` a package for testing.
- Added tests at `tests/test_main.py` covering `classify_orders` and `summarize_orders`.
- Will install and run `pytest` to validate tests.


Next steps:
- Run tests and fix any issues.
- Modularize code into smaller modules under `src/`.
- Add type hints, docstrings, and more tests.
- Add CI and README.

## 2026-06-07 (modularization)
- Split core logic into `src/processing.py`, `src/summary.py`, and `src/io.py`.
- Updated `src/main.py` to import from the new modules and kept CLI behavior.
- Updated tests to import from `src.processing` and `src.summary` and verified the simple test runner passes.

## 2026-06-07 (typing & docs)
- Added type hints and docstrings to `src/processing.py`, `src/summary.py`, `src/io.py`, and `src/main.py`.
- Verified tests still pass using the lightweight test runner.

## 2026-06-07 (CI)
- Added GitHub Actions workflow at `.github/workflows/ci.yml` to run tests on push and pull requests.
- Added `requirements.txt` with `pytest` so the workflow can install test dependencies.

## 2026-06-07 (README)
- Added `README.md` with project overview, usage examples, testing instructions, and development notes.

## 2026-06-07 (samples & notebook)
- Added sample dataset at `data/sample_orders.csv` for demo and testing purposes.
- Added a demo Jupyter notebook at `notebooks/demo.ipynb` that shows how to load the data, run processing, view cleaned/invalid rows, and plot revenue by product/customer.

## 2026-06-07 (interactive demo)
- Added `streamlit_app.py` to provide an interactive demo. The app accepts a CSV upload or uses `data/sample_orders.csv`, shows cleaned/invalid rows, and plots revenue by product and customer.
- Updated `requirements.txt` to include `streamlit`.

## 2026-06-07 (packaging)
- Added `pyproject.toml` with PEP 621 metadata and a console script entry point `csv-order-analyzer` referencing `src.main:main`.
- Updated `README.md` with local installation instructions and the CLI entry-point usage.

## 2026-06-07 (polishing)
- Created `PORTFOLIO_WRITEUP.md` with project overview, technical highlights, and interview talking points.
- Drafted a slide-by-slide presentation in `PRESENTATION.md`.
- Added `assets/screenshots/README.md` and `captions.txt` with instructions for capturing portfolio images.
