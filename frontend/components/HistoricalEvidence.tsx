import { BookOpenCheck, Database } from "lucide-react";

export default function HistoricalEvidence() {
  return <div className="panel"><div className="panel-title"><div className="icon-box"><BookOpenCheck size={18}/></div><div><h3>Historical evidence</h3><span>Signals retrieved for this recommendation</span></div></div>
    <div className="evidence-grid">
      <div className="evidence-card"><Database size={17}/><strong>Historical campaigns</strong><span>127 comparable campaigns</span></div>
      <div className="evidence-card"><strong>Audience match</strong><span>High similarity with prior conversion campaigns</span></div>
      <div className="evidence-card"><strong>Budget range</strong><span>Within observed high-efficiency range</span></div>
    </div>
  </div>;
}