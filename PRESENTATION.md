# Presentation Slide Draft — CSV Order Analyzer

Slide 1: Title
- CSV Order Analyzer
- Your Name — Purdue CS Applicant
- One-line summary: Clean, validate, and analyze order CSVs with tests, CI, and an interactive demo.

Slide 2: Problem
- CSVs are messy; data quality issues break downstream analysis.
- Need reliable pipelines to validate and summarize data.

Slide 3: Solution Overview
- A lightweight CLI + Streamlit app that validates, cleans, and reports on orders.
- Outputs: clean CSV, invalid rows CSV, duplicate rows CSV, and a human-readable summary.

Slide 4: Architecture
- `processing` (validation) -> `summary` (analytics) -> `io` (CSV output)
- Tests and CI ensure correctness; packaging makes it installable.

Slide 5: Demo screenshots / live demo
- Show Streamlit app screenshot and `summary.txt` sample.
- Show cleaned CSV preview.

Slide 6: Tech Stack
- Python, pandas, matplotlib, streamlit, pytest, GitHub Actions, setuptools/pyproject

Slide 7: Key Code Snippet
- Short example showing `classify_orders()` behavior and error classification.

Slide 8: Challenges & Learnings
- Validation edge cases, packaging, and designing for tests.

Slide 9: Next Steps
- More analytics, deployment, expand test coverage.

Slide 10: Q&A / Contact
- GitHub link
- Email

Notes:
- Keep slides visual; include charts from the demo and 2-3 annotated code snippets.
- Use speaker notes to rehearse explanations for validation logic and packaging decisions.
