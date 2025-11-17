# Coverage Reports

This directory contains HTML and XML coverage reports.

## Files (gitignored):
- `*.html` - Human-readable coverage reports
- `*.xml` - Machine-readable coverage data

## To regenerate:
```bash
pytest tests/test_HumanEval_54_spec_guided.py --cov=solutions --cov-branch --cov-report=html -v
```

Open `htmlcov/index.html` in your browser to view.
