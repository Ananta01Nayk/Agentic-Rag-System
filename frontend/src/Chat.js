import React, { useState } from "react";
import axios from "axios";
import "./Chat.css";

function Chat() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const sendQuestion = async () => {
    if (!question.trim()) return;

    setLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          question: question,
        }
      );

      setAnswer(response.data.answer);
    } catch (error) {
      setAnswer("⚠️ Backend connection error.");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <div className="chat-card">

        <h1>📄 AI PDF Chatbot</h1>
        <p className="subtitle">
          Ask questions from your uploaded PDF documents
        </p>

        <div className="input-section">
          <input
            type="text"
            placeholder="Ask anything from your PDF..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />

          <button onClick={sendQuestion}>
            {loading ? "Thinking..." : "Send"}
          </button>
        </div>

        {answer && (
          <div className="answer-box">
            <h3>Answer</h3>
            <p>{answer}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Chat;