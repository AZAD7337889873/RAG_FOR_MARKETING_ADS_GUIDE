from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]

SOURCE_FILE = (
    ROOT
    / "data"
    / "raw"
    / "campaigns.csv"
)

TARGET_FILE = (
    ROOT
    / "data"
    / "processed"
    / "campaigns.parquet"
)


REQUIRED_COLUMNS = [
    "campaign_id",
    "platform",
    "channel",
    "location",
    "audience",
    "campaign_type",
    "industry",
    "duration_days",
    "planned_budget",
    "spend",
    "impressions",
    "clicks",
    "conversions",
    "revenue",
]


NUMERIC_COLUMNS = [
    "duration_days",
    "planned_budget",
    "spend",
    "impressions",
    "clicks",
    "conversions",
    "revenue",
]


def validate_columns(df: pd.DataFrame):

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:

        raise ValueError(
            "Missing required columns: "
            f"{missing_columns}"
        )


def calculate_metrics(
    df: pd.DataFrame,
) -> pd.DataFrame:

    df["ctr"] = (
        df["clicks"]
        / df["impressions"].replace(0, pd.NA)
    )

    df["conversion_rate"] = (
        df["conversions"]
        / df["clicks"].replace(0, pd.NA)
    )

    df["cpc"] = (
        df["spend"]
        / df["clicks"].replace(0, pd.NA)
    )

    df["cpm"] = (
        df["spend"]
        / df["impressions"].replace(0, pd.NA)
        * 1000
    )

    df["roas"] = (
        df["revenue"]
        / df["spend"].replace(0, pd.NA)
    )

    df["remaining_budget"] = (
        df["planned_budget"]
        - df["spend"]
    )

    df["pacing_pct"] = (
        df["spend"]
        / df["planned_budget"].replace(0, pd.NA)
    )

    return df.fillna(0)


def load_data():

    if not SOURCE_FILE.exists():

        raise FileNotFoundError(
            f"Dataset not found: {SOURCE_FILE}"
        )

    print("Loading campaign CSV...")

    df = pd.read_csv(
        SOURCE_FILE
    )

    validate_columns(df)

    for column in NUMERIC_COLUMNS:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce",
        ).fillna(0)

    df = calculate_metrics(df)

    TARGET_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_parquet(
        TARGET_FILE,
        index=False,
    )

    print(
        f"Saved {len(df)} rows."
    )

    print(
        f"Parquet file: {TARGET_FILE}"
    )


if __name__ == "__main__":
    load_data()