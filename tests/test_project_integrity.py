
from pathlib import Path
import pandas as pd
import yaml

PROJECT = Path("/content/drive/MyDrive/EpiScope")
DATA = PROJECT / "data"

def test_config_exists():
    assert (PROJECT / "config.yaml").exists()

def test_config_is_valid():
    with open(PROJECT / "config.yaml", "r") as f:
        config = yaml.safe_load(f)
    assert config is not None

def test_silver_dataset():
    path = DATA / "silver" / "encounters"
    df = pd.read_parquet(path)

    assert len(df) == 9851
    assert "encounter_id" in df.columns
    assert "patient_id_hash" in df.columns
    assert "patient_id" not in df.columns
    assert df["encounter_id"].is_unique
    assert df["patient_id_hash"].notna().all()

def test_facility_registry():
    path = DATA / "raw" / "facility_registry" / "facility_registry.parquet"
    df = pd.read_parquet(path)

    assert len(df) == 640
    assert df["facility_id"].nunique() == 640
    assert df["district_code"].nunique() == 64

def test_weekly_summary():
    path = DATA / "gold" / "weekly_disease_summary"
    df = pd.read_parquet(path)

    assert len(df) == 8041
    assert df["district_code"].nunique() == 64
    assert df["disease"].nunique() == 4

    keys = ["district_code", "disease", "week_start"]
    assert not df.duplicated(keys).any()

def test_forecast_metrics():
    path = DATA / "gold" / "forecasting" / "forecast_metrics.csv"
    df = pd.read_csv(path)

    assert len(df) == 8
    assert df["MAE"].notna().all()

def test_dashboard_size_and_privacy():
    dashboard_data = PROJECT / "dashboard" / "data"
    files = list(dashboard_data.glob("*"))

    total_bytes = sum(
        f.stat().st_size for f in files if f.is_file()
    )

    assert total_bytes <= 10 * 1024 * 1024

    for file in files:
        if file.suffix.lower() in [".csv", ".json"]:
            content = file.read_text(
                encoding="utf-8",
                errors="ignore"
            ).lower()
            assert "patient_id_hash" not in content
            assert "patient_id" not in content
