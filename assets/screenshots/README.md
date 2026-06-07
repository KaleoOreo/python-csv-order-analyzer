Screenshot instructions

Please capture the following screenshots and add them to this folder as PNGs:

1. `streamlit_main.png` — Streamlit app main view showing cleaned orders and charts.
   - Run: `streamlit run streamlit_app.py` and navigate to the app in the browser.

2. `summary_txt.png` — A terminal showing the contents of `reports/summary.txt`.
   - Generate: `python src/main.py --input data/sample_orders.csv --reports-dir reports`
   - Then open `reports/summary.txt` and capture.

3. `clean_csv_preview.png` — Spreadsheet-like preview of `reports/clean_orders.csv` opened in Excel or VS Code.

4. `tests_run.png` — Terminal output showing `python run_tests.py` passing.

5. `package_install.png` — Terminal showing `python -m pip install -e .` and `csv-order-analyzer --help` output.

Naming conventions: use the filenames above. Keep image sizes reasonable (1200px wide). Add brief captions in a `captions.txt` file describing each image.
