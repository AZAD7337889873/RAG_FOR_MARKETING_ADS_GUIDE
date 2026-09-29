import type {
  CampaignInput,
  PredictionResult,
  RecommendationResult,
  SimulationResult,
} from "./types";

const API_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api";

async function request<T>(
  path: string,
  options?: RequestInit
): Promise<T> {
  const response = await fetch(`${API_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(options?.headers || {}),
    },
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(
      `API ${response.status}: ${errorText || response.statusText}`
    );
  }

  return response.json();
}

export const api = {
  predict: (data: CampaignInput) =>
    request<PredictionResult>("/predictions", {
      method: "POST",
      body: JSON.stringify(data),
    }),

  recommend: (data: CampaignInput) =>
    request<RecommendationResult>("/recommendations", {
      method: "POST",
      body: JSON.stringify(data),
    }),

  simulate: (data: {
    current_budget: number;
    new_budget: number;
    platform: string;
    ctr: number;
    conversion_rate: number;
    average_order_value: number;
  }) =>
    request<SimulationResult>("/simulations", {
      method: "POST",
      body: JSON.stringify(data),
    }),

  chat: (message: string) =>
    request<{ answer: string }>("/chat", {
      method: "POST",
      body: JSON.stringify({
        message,
        session_id: "default",
        top_k: 5,
      }),
    }),
};