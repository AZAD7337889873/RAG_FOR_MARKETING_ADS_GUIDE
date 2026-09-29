def allocate_budget(total_budget: float):
    weights = {
        "Google Ads": 0.35,
        "Meta Ads": 0.30,
        "TikTok Ads": 0.15,
        "LinkedIn Ads": 0.10,
        "Amazon Ads": 0.10,
    }

    return [
        {
            "platform": platform,
            "percentage": pct * 100,
            "budget": round(total_budget * pct, 2),
        }
        for platform, pct in weights.items()
    ]
