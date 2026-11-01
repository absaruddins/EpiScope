# EpiScope System Architecture

## 1. Overview
EpiScope is an academic prototype for district-level disease
surveillance, outbreak detection, forecasting and resource allocation
in Bangladesh.

## 2. Architecture Flow

```text
Reference Data       Raw Data
     |                  |
     +--------+---------+
              |
          BRONZE LAYER
       Quality checks
       Quarantine records
              |
          SILVER LAYER
    Clean and hashed encounters
              |
           GOLD LAYER
    +---------+----------+
    |         |          |
 Weekly     Outbreak   Forecasting
 Summary    Alerts         |
    |         |       Resource Allocation
    +---------+----------+
              |
       Aggregate CSV data
              |
        D3.js Dashboard
```

## 3. Data Sources

### Reference data
- Bangladesh district boundaries hosted by DGHS.
- District population data attributed to BBS 2022.
- Historical weather data from Open-Meteo.

### Synthetic data
- DHIS2-style encounter records.
- Facility registry.
- Ground-truth outbreak injection plan.
- Facility resource and stock snapshots.

## 4. Processing Layers

### Raw and Reference
Raw contains synthetic encounter and facility inputs.
Reference contains district, population and weather datasets.

### Bronze
Bronze stores quality reports and quarantined records.

### Silver
Silver contains clean encounter records. Patient identifiers
are hashed before the clean records are saved.

### Gold
Gold contains weekly disease summaries, outbreak alerts,
forecast outputs and resource allocation results.

## 5. Analytics Components

### Data quality
Seventeen quality rules check identifiers, facilities, districts,
dates, ages, ICD codes, reporting delays and duplicate records.

### Outbreak detection
The current prototype uses a previous-four-week baseline with
a standard-deviation threshold and a minimum threshold of 3 cases.

### Forecasting
Seasonal Naive forecasts are generated for dengue and diarrhoea
for horizons of one to four weeks.

### Resource allocation
Proportional allocation is compared with an integer linear
programming model using synthetic resource snapshots.

## 6. Dashboard
The D3.js v7 dashboard displays a district map, weekly trends,
outbreak alerts, forecasts and resource allocation comparisons.
District selection supports map zoom and highlighting.

## 7. Privacy and Limitations
Patient identifiers are hashed before clean Silver storage.
The hashing salt must remain outside the public repository.
The facility registry and stock snapshots are synthetic.
The current detection and forecasting methods are prototypes.
This system is not validated for real clinical decisions.

## 8. Pending Architecture Work
- Production-grade incremental Delta MERGE.
- Full-scale 25-million-row SF=1 generation.
- Scale-factor performance benchmarks.
- Automated tests and reproducible pipeline scripts.