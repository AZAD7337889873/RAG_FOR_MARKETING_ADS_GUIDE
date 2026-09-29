"use client";

import { useEffect, useState } from "react";
import {
  ArrowUpRight,
  Bot,
  CheckCircle2,
  Sparkles,
} from "lucide-react";

import { api } from "../lib/api";
import type {
  PredictionResult,
  RecommendationResult,
} from "../lib/types";

import PredictionCards from "./PredictionCards";
import BudgetAllocation from "./BudgetAllocation";
import PlatformComparison from "./PlatformComparison";
import HistoricalEvidence from "./HistoricalEvidence";

const demoPrediction: PredictionResult = {
  predicted_clicks: 4820,
  predicted_conversions: 216,
  predicted_revenue: 28450,
  predicted_roas: 2.85,
};

const demoRecommendation: RecommendationResult = {
  platform: [
    {
      platform: "Google Ads",
      strength: "high-intent search",
      typical_use: "conversion intent",
    },
    {
      platform: "Meta Ads",
      strength: "audience targeting",
      typical_use: "awareness and conversions",
    },
  ],

  budget_allocation: [
    {
      platform: "Google Ads",
      percentage: 35,
      budget: 3500,
    },
    {
      platform: "Meta Ads",
      percentage: 30,
      budget: 3000,
    },
    {
      platform: "TikTok Ads",
      percentage: 15,
      budget: 1500,
    },
    {
      platform: "LinkedIn Ads",
      percentage: 10,
      budget: 1000,
    },
    {
      platform: "Amazon Ads",
      percentage: 10,
      budget: 1000,
    },
  ],

  campaign_recommendations: [
    {
      area: "CTR",
      recommendation:
        "Test multiple creative variants, stronger headlines, and clearer calls to action.",
    },
    {
      area: "Conversion",
      recommendation:
        "Align landing-page messaging with the ad promise and reduce conversion friction.",
    },
    {
      area: "Budget",
      recommendation:
        "Use historical performance to rebalance budget toward campaigns supporting the ROAS objective.",
    },
    {
      area: "Measurement",
      recommendation:
        "Monitor spend, clicks, conversions, revenue, ROAS, CTR, CPC, and pacing together.",
    },
  ],
};

export default function ResultsDashboard() {
  const [prediction, setPrediction] =
    useState<PredictionResult>(demoPrediction);

  const [recommendation, setRecommendation] =
    useState<RecommendationResult>(demoRecommendation);

  const [campaign, setCampaign] =
    useState<Record<string, unknown>>({});

  useEffect(() => {
    const raw = sessionStorage.getItem("campaignInput");

    const input = raw ? JSON.parse(raw) : {};

    setCampaign(input);

    if (!raw) {
      return;
    }

    api
      .predict(input)
      .then((result) => {
        setPrediction(result);
      })
      .catch((error) => {
        console.error("Prediction API failed:", error);
      });

    api
      .recommend(input)
      .then((result) => {
        setRecommendation(result);
      })
      .catch((error) => {
        console.error("Recommendation API failed:", error);
      });
  }, []);

  const totalRecommendedBudget =
    recommendation.budget_allocation.reduce(
      (sum, item) => sum + item.budget,
      0
    );

  return (
    <div className="stack">

      {/* Campaign context */}
      <div className="result-context">

        <div>
          <span>Scenario</span>

          <strong>
            {String(
              campaign.campaign_name ||
                "Q4 Performance Campaign"
            )}
          </strong>
        </div>

        <div>
          <span>Platform</span>

          <strong>
            {String(
              campaign.platform ||
                "Meta Ads"
            )}
          </strong>
        </div>

        <div>
          <span>Budget</span>

          <strong>
            $
            {Number(
              campaign.budget || 10000
            ).toLocaleString()}
          </strong>
        </div>

        <div>
          <span>Confidence</span>

          <strong>--</strong>
        </div>

      </div>

      {/* Prediction cards */}
      <PredictionCards
        prediction={prediction}
      />

      <div className="two-col">

        {/* Budget allocation */}
        <BudgetAllocation
          recommendation={recommendation}
        />

        {/* AI recommendation */}
        <div className="panel recommendation-panel">

          <div className="panel-title">

            <div className="icon-box">
              <Sparkles size={18} />
            </div>

            <div>
              <h3>AI recommendation</h3>
              <span>Decision summary</span>
            </div>

          </div>

          <p className="large-copy">
            Recommended budget allocation based on
            historical performance signals and the
            selected campaign objective.
          </p>

          <div className="recommendation-target">

            <CheckCircle2 size={18} />

            <div>
              <span>
                Recommended allocation
              </span>

              <strong>
                {recommendation.budget_allocation.length}{" "}
                platforms
              </strong>
            </div>

            <b>
              $
              {totalRecommendedBudget.toLocaleString()}
            </b>

          </div>

          <ul className="reason-list">

            {recommendation.campaign_recommendations.map(
              (item, index) => (
                <li key={index}>

                  <ArrowUpRight size={15} />

                  <span>
                    <strong>
                      {item.area}:
                    </strong>{" "}
                    {item.recommendation}
                  </span>

                </li>
              )
            )}

          </ul>

        </div>

      </div>

      {/* Platform comparison */}
      <PlatformComparison />

      {/* Historical evidence */}
      <HistoricalEvidence />

      {/* Architecture explanation */}
      <div className="panel evidence-footer">

        <Bot size={20} />

        <div>

          <strong>
            How this answer is produced
          </strong>

          <span>
            Historical campaign data → ML predictions →
            recommendation rules → RAG evidence →
            Ollama-generated explanation.
          </span>

        </div>

      </div>

    </div>
  );
}