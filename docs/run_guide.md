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

## 8. Important Limitations
- This guide documents the verified prototype outputs.
- A complete one-command pipeline is not yet available.
- The 25-million-row SF=1 dataset has not been generated.
- Scale-factor benchmarks have not been completed.
- Incremental merge and outage recovery are simulations.
- Facility and stock data are synthetic.

Do not interpret prototype alerts, forecasts or resource allocations
as validated clinical or operational recommendations.