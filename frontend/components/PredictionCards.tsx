"use client";

import {
  MousePointerClick,
  ShoppingCart,
  DollarSign,
  TrendingUp,
} from "lucide-react";

import type { PredictionResult } from "../lib/types";

export default function PredictionCards({
  prediction,
}: {
  prediction: PredictionResult;
}) {
  const cards = [
    {
      label: "Expected Clicks",
      value: Math.round(prediction.predicted_clicks).toLocaleString(),
      icon: MousePointerClick,
    },
    {
      label: "Expected Conversions",
      value: Math.round(
        prediction.predicted_conversions
      ).toLocaleString(),
      icon: ShoppingCart,
    },
    {
      label: "Expected Revenue",
      value: `$${Math.round(
        prediction.predicted_revenue
      ).toLocaleString()}`,
      icon: DollarSign,
    },
    {
      label: "Expected ROAS",
      value: `${prediction.predicted_roas.toFixed(2)}x`,
      icon: TrendingUp,
    },
  ];

  return (
    <div className="metric-grid">
      {cards.map(({ label, value, icon: Icon }) => (
        <div className="metric-card" key={label}>
          <div className="metric-icon">
            <Icon size={19} />
          </div>

          <span>{label}</span>

          <strong>{value}</strong>
        </div>
      ))}
    </div>
  );
}