# EpiScope Run Guide

## 1. Requirements
- Google Colab
- Google Drive
- Python
- Java 17
- PySpark
- PyArrow
- Pandas
- PuLP

## 2. Open the Project
Mount Google Drive in Google Colab:

```python
from google.colab import drive
drive.mount('/content/drive')
```

Set the project directory:

```python
from pathlib import Path
PROJECT = Path('/content/drive/MyDrive/EpiScope')
```

## 3. Configuration
The main configuration file is `config.yaml`.
A copy is also stored at `config/config.yaml`.
Review paths, random seed, date range and scale-factor settings
before running data-generation tasks.

## 4. Data Locations
- Raw inputs: `data/raw/`
- Reference data: `data/reference/`
- Bronze outputs: `data/bronze/`
- Clean Silver data: `data/silver/`
- Gold analytical outputs: `data/gold/`
- Dashboard: `dashboard/`

## 5. Current Verified Outputs
- Clean encounters: `data/silver/encounters/`
- Weekly summary: `data/gold/weekly_disease_summary/`
- Outbreak alerts: `data/gold/outbreak_alerts/`
- Forecasts: `data/gold/forecasting/`
- Resource allocation: `data/gold/resource_allocation/`
- Dashboard HTML: `dashboard/index.html`

## 6. Open the Dashboard
Start a local web server from the project directory:

```bash
python -m http.server 8000
```

Then open:

`http://localhost:8000/dashboard/`

In Google Colab, use the Colab port proxy for port 8000.

## 7. Reproducibility
The project configuration defines random seed 42.
The synthetic patient-ID hashing salt must be supplied securely
and must not be committed to the repository.

## 8. Verified Scale Benchmarks

| Scale Factor | Total Rows | Read Time | Aggregation Time |
|---|---:|---:|---:|
| 0.25 | 6,375,000 | 11.42 sec | 13.47 sec |
| 0.50 | 12,750,000 | 13.22 sec | 6.46 sec |
| 1.00 | 25,500,000 | 13.78 sec | 12.76 sec |

The SF=1.00 dataset contains 25 million base rows and 25.5 million total rows including duplicates. All three scale-factor datasets were verified.

## 9. Automated Tests and Reports

- Automated tests: 7 passed.
- Technical Report: prepared and uploaded to reports/ (user-confirmed).
- Ministry Policy Brief: prepared and uploaded to reports/ (user-confirmed).
- Traceability Matrix: CSV and Markdown versions updated.

## 10. Remaining Work

- Production-grade Delta MERGE.
- Improved and validated outbreak detection.
- Additional forecasting model comparisons and interval validation.
- Complete reproducible pipeline scripts and monitoring.
- Required project presentation video.

## 11. Important Limitations

- Incremental merge and outage recovery are simulations.
- Facility and stock data are synthetic.
- Outbreak detection is a simple threshold prototype.
- Forecasting uses Seasonal Naive only.
- The large-scale generator does not include all reporting-delay fields used in the smaller prototype.

Do not interpret prototype alerts, forecasts or resource allocations as validated clinical or operational recommendations.
