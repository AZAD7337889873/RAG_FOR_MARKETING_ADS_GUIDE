from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]

OUTPUT_FILE = ROOT / "data" / "raw" / "campaigns.csv"


PLATFORMS = [
    "Google Ads",
    "Meta Ads",
    "TikTok Ads",
    "LinkedIn Ads",
    "Amazon Ads",
]

CHANNELS = [
    "Search",
    "Display",
    "Social",
    "Video",
    "Shopping",
]

LOCATIONS = [
    "UAE",
    "Saudi Arabia",
    "Qatar",
    "Kuwait",
    "Bahrain",
    "Oman",
    "Egypt",
]

AUDIENCES = [
    "18-24",
    "25-34",
    "35-44",
    "45-54",
    "55+",
]

CAMPAIGN_TYPES = [
    "Awareness",
    "Traffic",
    "Lead Generation",
    "Conversions",
    "Sales",
]

INDUSTRIES = [
    "Retail",
    "E-commerce",
    "Travel",
    "Finance",
    "Technology",
    "Healthcare",
]


PLATFORM_CTR = {
    "Google Ads": 0.032,
    "Meta Ads": 0.018,
    "TikTok Ads": 0.014,
    "LinkedIn Ads": 0.010,
    "Amazon Ads": 0.026,
}


PLATFORM_CVR = {
    "Google Ads": 0.055,
    "Meta Ads": 0.038,
    "TikTok Ads": 0.028,
    "LinkedIn Ads": 0.045,
    "Amazon Ads": 0.062,
}


PLATFORM_CPM = {
    "Google Ads": 18,
    "Meta Ads": 11,
    "TikTok Ads": 8,
    "LinkedIn Ads": 28,
    "Amazon Ads": 15,
}


def generate_campaign_data(
    number_of_campaigns: int = 600,
    seed: int = 42,
) -> pd.DataFrame:

    rng = np.random.default_rng(seed)

    rows = []

    for campaign_number in range(1, number_of_campaigns + 1):

        platform = rng.choice(PLATFORMS)

        channel = rng.choice(CHANNELS)

        location = rng.choice(LOCATIONS)

        audience = rng.choice(AUDIENCES)

        campaign_type = rng.choice(CAMPAIGN_TYPES)

        industry = rng.choice(INDUSTRIES)

        duration_days = int(
            rng.integers(
                low=7,
                high=61,
            )
        )

        planned_budget = rng.uniform(
            2000,
            100000,
        )

        spend_ratio = rng.uniform(
            0.45,
            1.05,
        )

        spend = planned_budget * spend_ratio

        impressions = (
            spend
            / PLATFORM_CPM[platform]
            * 1000
            * rng.uniform(0.80, 1.20)
        )

        clicks = (
            impressions
            * PLATFORM_CTR[platform]
            * rng.uniform(0.65, 1.35)
        )

        conversions = (
            clicks
            * PLATFORM_CVR[platform]
            * rng.uniform(0.65, 1.35)
        )

        average_order_value = rng.uniform(
            80,
            450,
        )

        revenue = (
            conversions
            * average_order_value
            * rng.uniform(0.75, 1.35)
        )

        rows.append(
            {
                "campaign_id": f"CMP-{campaign_number:04d}",
                "platform": platform,
                "channel": channel,
                "location": location,
                "audience": audience,
                "campaign_type": campaign_type,
                "industry": industry,
                "duration_days": duration_days,
                "planned_budget": round(planned_budget, 2),
                "spend": round(spend, 2),
                "impressions": int(impressions),
                "clicks": int(clicks),
                "conversions": int(max(0, conversions)),
                "revenue": round(max(0, revenue), 2),
            }
        )

    df = pd.DataFrame(rows)

    return calculate_metrics(df)


def calculate_metrics(df: pd.DataFrame) -> pd.DataFrame:

    df["ctr"] = (
        df["clicks"]
        / df["impressions"].replace(0, np.nan)
    )

    df["conversion_rate"] = (
        df["conversions"]
        / df["clicks"].replace(0, np.nan)
    )

    df["cpc"] = (
        df["spend"]
        / df["clicks"].replace(0, np.nan)
    )

    df["cpm"] = (
        df["spend"]
        / df["impressions"].replace(0, np.nan)
        * 1000
    )

    df["roas"] = (
        df["revenue"]
        / df["spend"].replace(0, np.nan)
    )

    df["remaining_budget"] = (
        df["planned_budget"]
        - df["spend"]
    )

    df["pacing_pct"] = (
        df["spend"]
        / df["planned_budget"].replace(0, np.nan)
    )

    df = df.fillna(0)

    return df


def main():

    print("Generating campaign dataset...")

    df = generate_campaign_data()

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False,
    )

    print(
        f"Generated {len(df)} campaigns."
    )

    print(
        f"Saved to: {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()