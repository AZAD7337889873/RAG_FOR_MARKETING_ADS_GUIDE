"use client";

import { useState } from "react";
import {
  Calculator,
  RefreshCw,
  TrendingUp,
} from "lucide-react";

import { api } from "../lib/api";
import type { SimulationResult } from "../lib/types";

export default function WhatIfSimulator() {
  const [currentBudget] = useState(10000);
  const [budget, setBudget] = useState(10000);

  const [platform, setPlatform] =
    useState("Meta Ads");

  const [duration, setDuration] =
    useState(30);

  const [result, setResult] =
    useState<SimulationResult | null>(null);

  const [loading, setLoading] =
    useState(false);

  async function simulate() {
    setLoading(true);

    const input = {
      current_budget: currentBudget,
      new_budget: budget,
      platform: platform,
      ctr: 0.025,
      conversion_rate: 0.04,
      average_order_value: 100,
    };

    try {
      const simulation = await api.simulate(input);

      setResult(simulation);
    } catch (error) {
      console.error(
        "Simulation API failed:",
        error
      );

      setResult(null);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="simulator-grid">

      {/* Scenario inputs */}
      <div className="panel">

        <div className="panel-title">

          <div className="icon-box">
            <Calculator size={18} />
          </div>

          <div>
            <h3>Scenario inputs</h3>
            <span>
              Adjust one variable at a time
            </span>
          </div>

        </div>

        {/* Platform */}
        <label>
          <span>Platform</span>

          <select
            value={platform}
            onChange={(e) =>
              setPlatform(e.target.value)
            }
          >
            <option>Meta Ads</option>
            <option>Google Ads</option>
            <option>TikTok Ads</option>
            <option>LinkedIn Ads</option>
            <option>Amazon Ads</option>
          </select>
        </label>

        {/* Budget */}
        <label>
          <span>
            Budget: $
            {budget.toLocaleString()}
          </span>

          <input
            type="range"
            min="1000"
            max="50000"
            step="500"
            value={budget}
            onChange={(e) =>
              setBudget(
                Number(e.target.value)
              )
            }
          />
        </label>

        {/* Duration */}
        <label>
          <span>
            Duration: {duration} days
          </span>

          <input
            type="range"
            min="7"
            max="90"
            value={duration}
            onChange={(e) =>
              setDuration(
                Number(e.target.value)
              )
            }
          />
        </label>

        {/* Current budget */}
        <div className="simulation-info">
          <span>Current budget</span>

          <strong>
            ${currentBudget.toLocaleString()}
          </strong>
        </div>

        {/* Run simulation */}
        <button
          className="btn primary full"
          onClick={simulate}
          disabled={loading}
        >
          {loading
            ? "Running..."
            : "Run simulation"}

          <TrendingUp size={17} />
        </button>

      </div>

      {/* Simulation result */}
      <div className="panel simulation-result">

        <div className="panel-title">

          <div className="icon-box">
            <RefreshCw size={18} />
          </div>

          <div>
            <h3>Projected outcome</h3>
            <span>
              Scenario result
            </span>
          </div>

        </div>

        {!result ? (

          <div className="empty-state">
            Run a scenario to see projected
            performance.
          </div>

        ) : (

          <div className="simulation-metrics">

            <div>
              <span>Expected clicks</span>

              <strong>
                {result.simulated.clicks.toLocaleString()}
              </strong>
            </div>

            <div>
              <span>Conversions</span>

              <strong>
                {result.simulated.conversions.toLocaleString()}
              </strong>
            </div>

            <div>
              <span>Revenue</span>

              <strong>
                $
                {result.simulated.revenue.toLocaleString()}
              </strong>
            </div>

            <div>
              <span>ROAS</span>

              <strong>
                {result.simulated.revenue > 0
                  ? (
                      result.simulated.revenue /
                      result.budget_change
                    ).toFixed(2)
                  : "0.00"}
                x
              </strong>
            </div>

          </div>

        )}

      </div>

    </div>
  );
}