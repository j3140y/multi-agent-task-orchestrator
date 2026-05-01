# 🚀 Multi-Agent Task Orchestration System (MVP)

A lightweight yet extensible multi-agent system built with LLMs, designed to automatically decompose, execute, and validate complex tasks through collaborative agents.

---

## 🧠 Overview

This project implements a **multi-agent architecture** that simulates autonomous task execution.
It is composed of four core agents:

* **Planner Agent** → Decomposes complex tasks into actionable steps
* **Executor Agent** → Executes each step using reasoning + LLM
* **Tool Agent** → Handles external tool interactions (search, compute, etc.)
* **Reviewer Agent** → Evaluates results and provides feedback

Together, they form a **closed-loop system** with planning, execution, and reflection.

---

## ⚙️ Architecture

User Task
↓
Planner Agent (Task Decomposition)
↓
Executor Agent (Step Execution)
↓
Tool Agent (External Tools)
↓
Reviewer Agent (Validation & Feedback)

---

## ✨ Features

* 🔹 Multi-agent collaboration (Planner / Executor / Reviewer / Tool)
* 🔹 Automatic task decomposition
* 🔹 Tool-augmented execution (extensible)
* 🔹 Self-reflection and result validation
* 🔹 Lightweight and easy to extend

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

Create environment file:

```bash
cp .env.example .env
```

Add your API key:

```
OPENAI_API_KEY=your_api_key
```

---

## 🚀 Usage

```bash
python main.py
```

Example task:

```
Analyze the reasons for user growth decline and provide optimization strategies.
```

---

## 🧪 Example Output

* Task decomposition (Planner)
* Step-by-step execution (Executor)
* Tool usage simulation
* Final evaluation (Reviewer)

---

## 📊 Project Value

This system demonstrates how LLMs can be orchestrated to:

* Reduce manual task decomposition effort
* Automate multi-step workflows
* Improve execution efficiency through reasoning
* Enable self-correcting systems via reflection

---

## 🔮 Future Work

* [ ] Add memory module (long-term context)
* [ ] Integrate real tools (API / database / search engines)
* [ ] Build a web-based UI
* [ ] Upgrade to LangChain / CrewAI framework
* [ ] Support multi-turn autonomous execution

---

## 📌 Tech Stack

* Python
* OpenAI API
* dotenv

---

## 🤝 Contributing

Feel free to fork, improve, and submit PRs!

---

## 📄 License

MIT License
