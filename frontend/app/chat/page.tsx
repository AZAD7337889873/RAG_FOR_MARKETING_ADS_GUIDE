import ChatBox from "../../components/ChatBox";

export default function ChatPage() {
  return (
    <main className="page-shell">
      <div className="page-header">
        <div><span className="section-kicker">AI ADVISOR</span><h1>Ask the marketing advisor</h1>
        <p>Ask about platforms, budget, campaign strategy, historical evidence or optimization.</p></div>
      </div>
      <ChatBox />
    </main>
  );
}