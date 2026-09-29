def build_features(data: dict) -> dict:
    budget = float(data.get("budget", 0))
    duration = int(data.get("duration_days", 30))
    return {
        "budget": budget,
        "duration_days": duration,
        "daily_budget": budget / max(duration, 1),
        "platform": data.get("platform", "Unknown"),
        "campaign_type": data.get("campaign_type", "Unknown"),
    }
