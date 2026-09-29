from pathlib import Path
import pandas as pd
from backend.app.config.settings import settings

class CampaignService:
    def _load(self):
        parquet = Path(settings.campaigns_parquet)
        csv = Path(settings.campaigns_csv)

        if parquet.exists():
            return pd.read_parquet(parquet)
        if csv.exists():
            return pd.read_csv(csv)
        return pd.DataFrame()

    def get_campaigns(self, limit=100):
        df = self._load().head(limit)
        return df.where(pd.notnull(df), None).to_dict(orient="records")

    def get_campaign(self, campaign_id):
        df = self._load()
        if df.empty:
            return None

        candidates = ["Campaign_ID", "campaign_id", "CampaignId"]
        col = next((c for c in candidates if c in df.columns), None)
        if not col:
            return None

        row = df[df[col].astype(str) == str(campaign_id)]
        if row.empty:
            return None
        return row.iloc[0].where(pd.notnull(row.iloc[0]), None).to_dict()

    def summary(self):
        df = self._load()
        if df.empty:
            return {"campaigns": 0}

        return {
            "campaigns": int(len(df)),
            "columns": list(df.columns),
            "numeric_summary": df.select_dtypes(include="number").describe().round(2).to_dict(),
        }
