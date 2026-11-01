# EpiScope
## Bangladesh Disease Surveillance, Forecasting and Resource Allocation

EpiScope is an academic prototype for Bangladesh disease surveillance.
It combines district reference data, weather data, synthetic encounters,
outbreak detection, forecasting and resource allocation.

## 1. Objectives
- Prepare district-level disease surveillance data.
- Simulate health encounters and reporting delays.
- Apply data-quality checks and quarantine invalid records.
- Hash patient identifiers before clean Silver storage.
- Generate weekly disease summaries.
- Detect potential outbreak signals.
- Forecast dengue and diarrhoea for 1-4 weeks.
- Compare proportional and LP resource allocation.
- Display results in a D3.js dashboard.

## 2. Technology
- Python, Google Colab and PySpark
- Pandas, GeoPandas and PyArrow
- Parquet
- PuLP
- D3.js v7
- Open-Meteo historical weather data

## 3. Repository Structure
```text
EpiScope/
  config/
  data/raw/
  data/reference/
  data/bronze/
  data/silver/
  data/gold/
  dashboard/
  src/
  tests/
  reports/
  docs/
  config.yaml
  README.md
```

## 4. Data Sources
- District boundaries: DGHS-hosted reference data.
- Population: BBS 2022-attributed ArcGIS data.
- Weather: Open-Meteo historical weather data.
- Synthetic encounters, facilities and resource snapshots.

## 5. Pipeline
- Raw: synthetic encounters and facility registry.
- Reference: boundaries, population and weather.
- Bronze: quality reports and quarantine.
- Silver: clean encounters with hashed patient identifiers.
- Gold: weekly summaries, alerts, forecasts and allocation.

## 6. Verified Prototype Results
| Item | Result |
|---|---:|
| Districts | 64 |
| Synthetic facilities | 640 |
| Encounter rows including duplicates | 10,200 |
| Clean Silver rows | 9,851 |
| Quarantined rows | 349 |
| Weekly Gold rows | 8,041 |
| Weekly outbreak records | 67,072 |
| Alert records | 64 |
| Forecast rows | 512 |
| Resource allocation rows | 1,280 |
| Dashboard data size | 1.08 MB |

## 7. Analytical Methods
- Data quality: 17 implemented checks.
- Privacy: SHA-256 patient identifier hashing.
- Outbreak detection: previous-four-week mean and standard deviation
  with a minimum threshold of 3 cases.
- Forecasting: Seasonal Naive for dengue and diarrhoea.
- Resource allocation: proportional baseline and integer LP model.

## 8. Dashboard
The D3.js v7 dashboard contains:
1. District disease map.
2. Weekly disease trend.
3. Outbreak alerts.
4. Four-week forecast.
5. Resource allocation comparison.

Run locally from the project directory:
```bash
python -m http.server 8000
```
Open http://localhost:8000/dashboard/

## 9. Pending Requirements
- Generate and verify the 25-million-row SF=1 dataset.
- Run SF 0.25, 0.5 and 1.0 benchmarks.
- Improve and evaluate outbreak detection methods.
- Compare additional forecasting models.
- Validate prediction intervals and WIS.
- Complete automated tests and pipeline scripts.
- Complete technical report and Ministry policy brief.
- Record the required project presentation video.

## 10. Limitations
This is an academic prototype, not a production surveillance system.
Facility and stock data are synthetic.
The outbreak detector is a simple prototype threshold method.
The forecasting method currently uses Seasonal Naive.
The resource allocation results are not clinical recommendations.

## 11. Responsible Use
Do not use synthetic data, prototype alerts or forecasts for real
clinical decisions or operational resource deployment.