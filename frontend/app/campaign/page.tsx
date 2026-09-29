import CampaignForm from "../../components/CampaignForm";

export default function CampaignPage() {
  return (
    <main className="page-shell">
      <div className="page-header">
        <div><span className="section-kicker">CAMPAIGN PLANNER</span><h1>Build a campaign scenario</h1>
        <p>Provide the campaign inputs used by the prediction and recommendation services.</p></div>
      </div>
      <CampaignForm />
    </main>
  );
}