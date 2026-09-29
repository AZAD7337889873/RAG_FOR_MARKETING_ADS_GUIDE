"use client";

import { BarChart3 } from "lucide-react";
const rows = [
  ["Meta Ads", "4,820", "216", "$2.07", "2.85x"],
  ["Google Ads", "4,160", "188", "$2.40", "2.62x"],
  ["TikTok Ads", "5,340", "154", "$1.87", "2.18x"],
  ["LinkedIn Ads", "2,110", "81", "$4.74", "1.92x"],
];

export default function PlatformComparison() {
  return <div className="panel"><div className="panel-title"><div className="icon-box"><BarChart3 size={18}/></div><div><h3>Platform comparison</h3><span>Illustrative scenario estimates</span></div></div>
    <div className="table-wrap"><table><thead><tr><th>Platform</th><th>Clicks</th><th>Conversions</th><th>CPC</th><th>ROAS</th></tr></thead><tbody>{rows.map(r => <tr key={r[0]}>{r.map((c,i)=><td key={i} className={i===4?"strong-cell":""}>{c}</td>)}</tr>)}</tbody></table></div>
  </div>;
}