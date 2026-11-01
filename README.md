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
| Automated tests | 7 passed |

## 7. Analytical Methods
- Data quality: 17 implemented checks.
- Privacy: SHA-256 patient identifier hashing.
- Outbreak detection: previous-four-week mean and standard deviation
  with a minimum threshold of 3 cases.
- Forecasting: Seasonal Naive for dengue and diarrhoea.
- Resource allocation: proportional baseline and integer LP model.

## 8. Scale Benchmarks and Evaluation

| Scale Factor | Total Rows | Read Time | Aggregation Time |
|---|---:|---:|---:|
| 0.25 | 6,375,000 | 11.42 sec | 13.47 sec |
| 0.50 | 12,750,000 | 13.22 sec | 6.46 sec |
| 1.00 | 25,500,000 | 13.78 sec | 12.76 sec |

The outbreak evaluation detected 7 of 31 synthetic events (22.58% event sensitivity), with a median detection delay of 21 days. These results indicate that the detector needs improvement.

## 9. Dashboard
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

## 9. Remaining Requirements

- Implement production-grade Delta MERGE for incremental processing.
- Improve and validate outbreak detection methods.
- Compare additional forecasting models and validate prediction intervals and WIS.
- Complete reproducible pipeline scripts and operational monitoring.
- Record the required project presentation video.

Completed evidence:
- SF=0.25, 0.50 and 1.00 datasets generated and verified.
- SF=1.00 contains 25 million base rows and 25.5 million rows including duplicates.
- Spark scale benchmarks completed for all three scale factors.
- Automated test suite: 7 tests passed.
- Technical Report and Ministry Policy Brief prepared and uploaded (user-confirmed).

## 11. Limitations
This is an academic prototype, not a production surveillance system.
Facility and stock data are synthetic.
The outbreak detector is a simple prototype threshold method.
The forecasting method currently uses Seasonal Naive.
The resource allocation results are not clinical recommendations.

## 12. Responsible Use
Do not use synthetic data, prototype alerts or forecasts for real
clinical decisions or operational resource deployment.

## 10. Recent Engineering and Privacy Validation

### Delta Lake MERGE prototype
- Delta Lake 4.0.0 was configured successfully with Spark 4.0.4.
- An isolated Delta table was created from 9,851 Silver records.
- A MERGE test updated 2 existing records and inserted 3 new records.
- Final row count: 9,854, with 9,854 unique encounter IDs.
- Re-running the same source inserted no additional records or duplicates.
- This validates MERGE behavior in an isolated prototype, not production deployment.

### Privacy-safe dashboard
- Dashboard data files are served from `dashboard/data_safe/`.
- Small observed counts from 1 to 4 are suppressed in the weekly trend, district map and outbreak alerts.
- Related lab-confirmed and admitted counts are also suppressed.
- Alert indicators are hidden when the associated observed count is suppressed.
- Forecast values from 0 to 4 and their intervals are suppressed.
- Resource allocation values are retained because they represent resource units, not case counts.
- Original dashboard CSV files are preserved separately.

### Dashboard validation
- Dashboard HTML returned HTTP 200 from the local server.
- JavaScript syntax and safe data paths passed automated checks.
- Browser display was confirmed by the project user.

Note: Small-cell suppression reduces direct disclosure risk but does not guarantee anonymity. Complementary suppression and aggregation/differencing risks require further review.
