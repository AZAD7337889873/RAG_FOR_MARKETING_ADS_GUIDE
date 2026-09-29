"use client";

import { FormEvent, useState } from "react";
import { useRouter } from "next/navigation";
import {
  ArrowRight,
  CalendarDays,
  DollarSign,
  Megaphone,
  Users,
} from "lucide-react";

const defaults = {
  campaign_name: "Q4 Performance Campaign",
  objective: "Conversions",
  platform: "Meta Ads",
  audience: "Adults 25-44",
  location: "UAE",
  budget: 10000,
  duration_days: 30,
};

export default function CampaignForm() {
  const router = useRouter();

  const [form, setForm] = useState(defaults);
  const [loading, setLoading] = useState(false);

  function update(
    key: keyof typeof defaults,
    value: string | number
  ) {
    setForm((current) => ({
      ...current,
      [key]: value,
    }));
  }

  function submit(e: FormEvent) {
    e.preventDefault();

    setLoading(true);

    // Save campaign inputs for the Results page.
    sessionStorage.setItem(
      "campaignInput",
      JSON.stringify(form)
    );

    // Go directly to the results page.
    router.push("/results");
  }

  return (
    <form
      className="form-card"
      onSubmit={submit}
    >
      <div className="form-grid">

        <label>
          <span>Campaign name</span>

          <input
            value={form.campaign_name}
            onChange={(e) =>
              update(
                "campaign_name",
                e.target.value
              )
            }
          />
        </label>

        <label>
          <span>Objective</span>

          <select
            value={form.objective}
            onChange={(e) =>
              update(
                "objective",
                e.target.value
              )
            }
          >
            <option>Conversions</option>
            <option>Traffic</option>
            <option>Awareness</option>
            <option>Lead Generation</option>
            <option>Revenue</option>
          </select>
        </label>

        <label>
          <span>Platform</span>

          <select
            value={form.platform}
            onChange={(e) =>
              update(
                "platform",
                e.target.value
              )
            }
          >
            <option>Meta Ads</option>
            <option>Google Ads</option>
            <option>TikTok Ads</option>
            <option>LinkedIn Ads</option>
            <option>Amazon Ads</option>
          </select>
        </label>

        <label>
          <span>Target audience</span>

          <input
            value={form.audience}
            onChange={(e) =>
              update(
                "audience",
                e.target.value
              )
            }
          />
        </label>

        <label>
          <span>Location</span>

          <input
            value={form.location}
            onChange={(e) =>
              update(
                "location",
                e.target.value
              )
            }
          />
        </label>

        <label>
          <span>Budget</span>

          <div className="input-icon">
            <DollarSign size={16} />

            <input
              type="number"
              min="0"
              value={form.budget}
              onChange={(e) =>
                update(
                  "budget",
                  Number(e.target.value)
                )
              }
            />
          </div>
        </label>

        <label>
          <span>Duration (days)</span>

          <div className="input-icon">
            <CalendarDays size={16} />

            <input
              type="number"
              min="1"
              value={form.duration_days}
              onChange={(e) =>
                update(
                  "duration_days",
                  Number(e.target.value)
                )
              }
            />
          </div>
        </label>

      </div>

      <div className="form-summary">

        <div>
          <Megaphone size={19} />

          <div>
            <strong>
              {form.platform}
            </strong>

            <small>
              {form.objective} · {form.location}
            </small>
          </div>
        </div>

        <div>
          <Users size={19} />

          <div>
            <strong>
              {form.audience}
            </strong>

            <small>
              {form.duration_days} day campaign
            </small>
          </div>
        </div>

        <div>
          <DollarSign size={19} />

          <div>
            <strong>
              $
              {Number(
                form.budget
              ).toLocaleString()}
            </strong>

            <small>
              Total planned budget
            </small>
          </div>
        </div>

      </div>

      <button
        className="btn primary submit-btn"
        disabled={loading}
      >
        {loading
          ? "Analyzing..."
          : "Generate campaign analysis"}

        <ArrowRight size={17} />
      </button>

    </form>
  );
}