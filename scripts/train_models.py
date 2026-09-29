from pathlib import Path

import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


ROOT = Path(__file__).resolve().parents[1]

DATA_FILE = (
    ROOT
    / "data"
    / "processed"
    / "campaigns.parquet"
)

MODEL_DIRECTORY = (
    ROOT
    / "ml_models"
)


CATEGORICAL_COLUMNS = [
    "platform",
    "channel",
    "location",
    "audience",
    "campaign_type",
    "industry",
]


MODEL_CONFIG = {

    "click_model": {

        "target": "clicks",

        "features": [
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
        ],
    },

    "conversion_model": {

        "target": "conversions",

        "features": [
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
        ],
    },

    "revenue_model": {

        "target": "revenue",

        "features": [
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
        ],
    },

    "roas_model": {

        "target": "roas",

        "features": [
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
        ],
    },
}


def create_pipeline(features):

    categorical = [
        column
        for column in CATEGORICAL_COLUMNS
        if column in features
    ]

    numerical = [
        column
        for column in features
        if column not in categorical
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(
                    handle_unknown="ignore"
                ),
                categorical,
            ),
            (
                "numerical",
                "passthrough",
                numerical,
            ),
        ]
    )

    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=12,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1,
    )

    return Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor,
            ),
            (
                "model",
                model,
            ),
        ]
    )


def train_model(
    model_name,
    configuration,
    df,
):

    target = configuration["target"]

    features = configuration["features"]

    X = df[features]

    y = df[target].astype(float)

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
        )
    )

    pipeline = create_pipeline(
        features
    )

    print(
        f"Training {model_name}..."
    )

    pipeline.fit(
        X_train,
        y_train,
    )

    predictions = pipeline.predict(
        X_test
    )

    mae = mean_absolute_error(
        y_test,
        predictions,
    )

    artifact = {

        "model": pipeline,

        "model_name": model_name,

        "target": target,

        "features": features,

        "mae": float(mae),
    }

    MODEL_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file = (
        MODEL_DIRECTORY
        / f"{model_name}.pkl"
    )

    joblib.dump(
        artifact,
        output_file,
    )

    print(
        f"Saved: {output_file}"
    )

    print(
        f"MAE: {mae:.4f}"
    )


def main():

    if not DATA_FILE.exists():

        raise FileNotFoundError(
            "Processed dataset not found. "
            "Run scripts/load_data.py first."
        )

    df = pd.read_parquet(
        DATA_FILE
    )

    for model_name, configuration in (
        MODEL_CONFIG.items()
    ):

        train_model(
            model_name,
            configuration,
            df,
        )

    print(
        "All models trained successfully."
    )


if __name__ == "__main__":
    main()