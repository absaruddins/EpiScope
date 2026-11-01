# EpiScope Requirement Traceability Matrix

This matrix records the current implementation status. Pending items are not considered complete.

| Requirement | Current implementation | Status |
|---|---|---|
| District reference data | 64 district boundaries and population data | Verified |
| Weather data | 64 districts, 2021-2025 Open-Meteo data | Verified |
| Synthetic facility registry | 640 facilities across 64 districts | Verified |
| Synthetic encounter generator | 10,200 rows including injected defects | Prototype verified |
| Outbreak ground truth | 30 local events plus nationwide event | Verified |
| Seasonality and weather features | Disease-specific date weights and seasonal features | Prototype verified |
| Reporting delay and backfill | 0-21 day delay and 21-day silence simulation | Verified |
| Data quality | 17 checks and 349 quarantined rows | Verified |
| Patient privacy | SHA-256 patient ID hashing before clean Silver | Verified |
| Weekly Gold summary | 8,041 district-disease-week rows | Verified |
| Outbreak detection | Four-week baseline threshold; 64 alerts | Prototype; improvement pending |
| Detection evaluation | 22.58% event sensitivity; 0.1219 false alert weeks per district-year | Evaluated; improvement needed |
| Forecasting | Seasonal Naive, dengue and diarrhoea, 1-4 weeks | Prototype verified |
| Forecast backtesting | Rolling backtest with MAE, 80% coverage and WIS outputs | Prototype; validation pending |
| Resource snapshots | 640 synthetic facility snapshots | Verified |
| Proportional allocation | 494 demand units allocated | Verified |
| LP allocation | Optimal solution; 494 units allocated; 30 entries changed | Verified |
| Incremental processing | 21-day lookback and idempotency simulation | Simulation verified |
| 14-day outage recovery | All 9,851 clean records recovered in simulation | Simulation verified |
| D3 dashboard | Five coordinated views; district zoom and highlight | Browser verified |
| Dashboard size | 1.08 MB aggregate dashboard data | Verified |
| SF=1 25-million-row dataset | Target exists in config; dataset not generated | Pending |
| Scale factor benchmarks | SF 0.25, 0.5 and 1.0 benchmarks not run | Pending |
| Production Delta MERGE | Current incremental test uses Spark deduplication simulation | Pending |
| Automated test suite | Test folder exists; full automated suite not verified | Pending |
| Technical report | Not yet prepared | Pending |
| Ministry policy brief | Not yet prepared | Pending |
| Presentation video | Not yet recorded | Pending |