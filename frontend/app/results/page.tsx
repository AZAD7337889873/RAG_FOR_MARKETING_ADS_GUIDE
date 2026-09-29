import ResultsDashboard from "../../components/ResultsDashboard";

export default function ResultsPage() {
  return (
    <main className="page-shell">
      <div className="page-header">
        <div><span className="section-kicker">CAMPAIGN INTELLIGENCE</span><h1>Predictions & recommendations</h1>
        <p>Review projected performance and the evidence behind the recommendation.</p></div>
      </div>
      <ResultsDashboard />
    </main>
  );
}