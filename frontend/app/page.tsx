import Link from "next/link";
import { ArrowRight, BarChart3, Bot, Brain, DollarSign, Sparkles, Target, TrendingUp } from "lucide-react";

const cards = [
  { href: "/campaign", icon: Target, title: "Create Campaign", text: "Enter campaign objectives, audience, channel and budget." },
  { href: "/results", icon: TrendingUp, title: "Predictions & Recommendations", text: "Review expected clicks, conversions, revenue, ROAS and platform allocation." },
  { href: "/simulator", icon: DollarSign, title: "What-If Simulator", text: "Test budget changes and compare projected campaign outcomes." },
  { href: "/chat", icon: Bot, title: "AI Marketing Advisor", text: "Ask questions using historical data and the marketing knowledge base." },
];

export default function Home() {
  return (
    <main className="shell">
      <section className="hero">
        <div className="hero-copy">
          <div className="eyebrow"><Sparkles size={16} /> AI-powered media planning</div>
          <h1>Marketing AI <span>Advisor</span></h1>
          <p>
            Turn historical campaign data and marketing knowledge into practical
            campaign predictions, budget recommendations and AI-assisted decisions.
          </p>
          <div className="hero-actions">
            <Link className="btn primary" href="/campaign">Start Planning <ArrowRight size={17} /></Link>
            <Link className="btn secondary" href="/chat">Ask AI Advisor</Link>
          </div>
        </div>
        <div className="hero-panel">
          <div className="panel-glow" />
          <Brain size={46} />
          <h3>Decision Intelligence</h3>
          <p>ML predictions + business rules + RAG + Ollama</p>
          <div className="mini-stats">
            <div><strong>ML</strong><span>Predictions</span></div>
            <div><strong>RAG</strong><span>Evidence</span></div>
            <div><strong>LLM</strong><span>Advice</span></div>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="section-heading">
          <div><span className="section-kicker">WORKSPACE</span><h2>What do you want to do?</h2></div>
          <p>Each workflow is connected to your FastAPI backend.</p>
        </div>
        <div className="feature-grid">
          {cards.map(({ href, icon: Icon, title, text }) => (
            <Link href={href} className="feature-card" key={href}>
              <div className="icon-box"><Icon size={21} /></div>
              <h3>{title}</h3>
              <p>{text}</p>
              <span>Open workspace <ArrowRight size={15} /></span>
            </Link>
          ))}
        </div>
      </section>

      <section className="architecture-strip">
        <div><BarChart3 size={20} /><strong>Historical Data</strong><span>Campaign performance</span></div>
        <div><Brain size={20} /><strong>ML Models</strong><span>Clicks · Conversions · Revenue · ROAS</span></div>
        <div><Bot size={20} /><strong>RAG + Ollama</strong><span>Grounded marketing advice</span></div>
      </section>
    </main>
  );
}