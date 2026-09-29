"use client";

import { PieChart } from "lucide-react";
import type { RecommendationResult } from "../lib/types";

export default function BudgetAllocation({
  recommendation,
}: {
  recommendation: RecommendationResult;
}) {
  const allocations = recommendation.budget_allocation || [];

  const total = allocations.reduce(
    (sum, item) => sum + item.budget,
    0
  );

  return (
    <div className="panel">
      <div className="panel-title">
        <div className="icon-box">
          <PieChart size={18} />
        </div>

        <div>
          <h3>Recommended allocation</h3>
          <span>Based on expected efficiency</span>
        </div>
      </div>

      <div className="allocation">
        {allocations.map((item) => {
          const percentage =
            total > 0 ? Math.round((item.budget / total) * 100) : 0;

          return (
            <div className="allocation-main" key={item.platform}>
              <strong>{item.platform}</strong>

              <span>
                ${item.budget.toLocaleString()}
              </span>

              <div className="progress">
                <i
                  style={{
                    width: `${percentage}%`,
                  }}
                />
              </div>

              <small>{percentage}% of recommended budget</small>
            </div>
          );
        })}
      </div>
    </div>
  );
}