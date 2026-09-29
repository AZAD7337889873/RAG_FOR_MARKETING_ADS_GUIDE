"use client";

import { FormEvent, useState } from "react";
import { Bot, Send, UserRound } from "lucide-react";
import { api } from "../lib/api";

type Message = { role: "user" | "assistant"; content: string };

export default function ChatBox() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<Message[]>([
    { role: "assistant", content: "Hi! I can help with campaign strategy, platform selection, budget allocation, historical performance and optimization. What would you like to know?" }
  ]);
  const [loading, setLoading] = useState(false);

  async function send(e: FormEvent) {
    e.preventDefault();
    if (!input.trim()) return;
    const question = input.trim();
    setInput("");
    setMessages(m => [...m, { role: "user", content: question }]);
    setLoading(true);
    try {
      const result = await api.chat(question);
      setMessages(m => [...m, { role: "assistant", content: result.answer }]);
    } catch {
      setMessages(m => [...m, { role: "assistant", content: "The FastAPI backend is not reachable yet. Start the backend on http://localhost:8000 and try again." }]);
    } finally { setLoading(false); }
  }

  return <div className="chat-layout">
    <div className="panel chat-panel">
      <div className="chat-messages">{messages.map((m,i)=><div className={`message ${m.role}`} key={i}><div className="avatar">{m.role==="assistant"?<Bot size={17}/>:<UserRound size={17}/>}</div><div className="bubble">{m.content}</div></div>)}{loading && <div className="message assistant"><div className="avatar"><Bot size={17}/></div><div className="bubble typing">Thinking...</div></div>}</div>
      <form className="chat-input" onSubmit={send}><input placeholder="Ask: Which platform should I use for conversions?" value={input} onChange={e=>setInput(e.target.value)}/><button aria-label="Send"><Send size={18}/></button></form>
    </div>
    <aside className="panel chat-side"><h3>Try asking</h3>{["Which platform fits a conversion campaign?","How should I allocate a $20k budget?","Why is my CTR falling?","What historical evidence supports this recommendation?"].map(q=><button key={q} onClick={()=>setInput(q)}>{q}</button>)}</aside>
  </div>;
}