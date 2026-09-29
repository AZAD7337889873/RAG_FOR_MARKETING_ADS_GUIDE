def recommend_platform(data: dict):
    objective = data.get("objective", "ROAS").lower()

    profiles = {
        "google ads": {"strength": "high-intent search", "typical_use": "conversion intent"},
        "meta ads": {"strength": "audience targeting", "typical_use": "awareness and conversions"},
        "tiktok ads": {"strength": "short-form discovery", "typical_use": "reach and engagement"},
        "linkedin ads": {"strength": "professional targeting", "typical_use": "B2B lead generation"},
        "amazon ads": {"strength": "commerce intent", "typical_use": "product discovery and sales"},
    }

    if objective == "awareness":
        selected = ["meta ads", "tiktok ads"]
    elif objective == "b2b":
        selected = ["linkedin ads", "google ads"]
    elif objective == "sales":
        selected = ["google ads", "amazon ads"]
    else:
        selected = ["google ads", "meta ads"]

    return [{"platform": p.title(), **profiles[p]} for p in selected]
