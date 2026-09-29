from backend.app.schemas.simulation import SimulationRequest

class SimulationService:
    def simulate(self, request: SimulationRequest):
        current = request.current_budget
        new = request.new_budget
        ratio = new / current

        ctr = request.ctr or 0.02
        conversion_rate = request.conversion_rate or 0.03
        aov = request.average_order_value or 100

        current_clicks = current * ctr
        new_clicks = new * ctr
        current_conversions = current_clicks * conversion_rate
        new_conversions = new_clicks * conversion_rate
        current_revenue = current_conversions * aov
        new_revenue = new_conversions * aov

        return {
            "platform": request.platform,
            "budget_change": new - current,
            "budget_change_pct": round((ratio - 1) * 100, 2),
            "current": {
                "clicks": round(current_clicks, 2),
                "conversions": round(current_conversions, 2),
                "revenue": round(current_revenue, 2),
            },
            "simulated": {
                "clicks": round(new_clicks, 2),
                "conversions": round(new_conversions, 2),
                "revenue": round(new_revenue, 2),
            },
            "assumptions": {
                "ctr": ctr,
                "conversion_rate": conversion_rate,
                "average_order_value": aov,
            },
        }
