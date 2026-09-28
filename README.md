# Skill-to-Career Agent 🤖

An Agentic AI application that helps students understand **skill demand** and discover relevant **job opportunities**.

The agent uses Gemini to reason about the user's request and automatically selects the appropriate tools for researching industry demand and finding job openings.

## 🚀 Features

* 🔎 Skill demand and industry trend research
* 💼 Job search based on skill and location
* 🤖 AI Agent with tool calling
* 🌐 Tavily web search integration
* 📡 Job search API integration
* 🎯 Supports related job titles for a given skill
* 🔐 API keys managed using environment variables

## 🏗️ Architecture

```text
User Query
    ↓
Gemini
    ↓
LangChain Agent
    ↓
 ┌──────────────────────┐
 │                      │
 ▼                      ▼
Tavily Search       Job Search Tool
 │                      │
 ▼                      ▼
Industry Demand      Job Listings
 └──────────┬───────────┘
            ↓
          Gemini
            ↓
      Final Response
```

## 🛠️ Tech Stack

* Python
* LangChain
* LangGraph
* Google Gemini
* Tavily Search
* JSearch / RapidAPI
* REST APIs
* python-dotenv

## 📁 Project Structure

```text
Skill-to-Career-Agent/
│
├── app.py
├── .env
├── .gitignore
└── README.md
```

> `.env` contains API keys and should never be committed to GitHub.

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/skill-to-career-agent.git
cd skill-
```
