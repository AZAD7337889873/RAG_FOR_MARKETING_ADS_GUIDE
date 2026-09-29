export type CampaignInput = {
  campaign_name: string;
  objective: string;
  platform: string;
  audience: string;
  location: string;
  budget: number;
  duration_days: number;
};

export type PredictionResult = {
  predicted_clicks: number;
  predicted_conversions: number;
  predicted_revenue: number;
  predicted_roas: number;
};

export type PlatformRecommendation = {
  platform: string;
  strength: string;
  typical_use: string;
};

export type BudgetAllocation = {
  platform: string;
  percentage: number;
  budget: number;
};

export type CampaignRecommendation = {
  area: string;
  recommendation: string;
};

export type RecommendationResult = {
  platform: PlatformRecommendation[];
  budget_allocation: BudgetAllocation[];
  campaign_recommendations: CampaignRecommendation[];
};

export type SimulationResult = {
  platform: string;
  budget_change: number;
  budget_change_pct: number;
  current: {
    clicks: number;
    conversions: number;
    revenue: number;
  };
  simulated: {
    clicks: number;
    conversions: number;
    revenue: number;
  };
  assumptions: {
    ctr: number;
    conversion_rate: number;
    average_order_value: number;
  };
};