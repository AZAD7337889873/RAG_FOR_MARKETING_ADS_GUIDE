import WhatIfSimulator from "../../components/WhatIfSimulator";

export default function SimulatorPage() {
  return (
    <main className="page-shell">
      <div className="page-header">
        <div><span className="section-kicker">WHAT-IF ANALYSIS</span><h1>Budget simulator</h1>
        <p>Change budget assumptions and send the scenario to your simulation API.</p></div>
      </div>
      <WhatIfSimulator />
    </main>
  );
}