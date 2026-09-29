def campaign_recommendations(data: dict):
    objective = data.get("objective", "ROAS")

    return [
        {
            "area": "CTR",
            "recommendation": "Test multiple creative variants, stronger headlines, and clearer calls to action.",
        },
        {
            "area": "Conversion",
            "recommendation": "Align landing-page messaging with the ad promise and reduce conversion friction.",
        },
        {
            "area": "Budget",
            "recommendation": f"Use historical performance to rebalance budget toward campaigns supporting the {objective} objective.",
        },
        {
            "area": "Measurement",
            "recommendation": "Monitor spend, clicks, conversions, revenue, ROAS, CTR, CPC, and pacing together.",
        },
    ]
