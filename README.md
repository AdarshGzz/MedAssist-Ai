<div align="center">

<img src="docs/assets/hero-banner.svg" alt="MedAssist AI" width="100%"/>

# 🧬 MedAssist AI
**Advanced Clinical Intelligence & Diagnostics Platform**

[![React](https://img.shields.io/badge/React_19-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Ollama](https://img.shields.io/badge/Ollama_Local_AI-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.ai)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E)](https://vitejs.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

*An open-source, HIPAA-compliant clinical AI dashboard featuring local LLM inference, live ECG monitoring, federated learning, and FHIR interoperability.*

</div>

---

## ✨ Core Features & Capabilities

MedAssist AI is engineered from the ground up to provide state-of-the-art clinical intelligence while strictly adhering to privacy and performance standards. Below is a detailed breakdown of the platform's core capabilities:

### 🧠 1. Local-First AI Copilot (LangGraph & Ollama)
- **Zero-Data Leakage**: The entire LLM inference stack runs locally on your hardware using Ollama. Patient data never touches a public cloud, ensuring total HIPAA compliance out of the box.
- **Multi-Agent RAG**: Powered by LangGraph, the AI acts as a multi-agent system capable of retrieving medical guidelines, querying past patient electronic health records (EHR), and synthesizing actionable insights contextually.
- **Streaming Responses**: Real-time token streaming directly to the Vite frontend for a ChatGPT-like responsive experience.

### 📈 2. Real-Time Patient Telemetry & ECG Monitoring
- **OffscreenCanvas Architecture**: The dashboard features an advanced `OffscreenCanvas` rendering engine built into React 19, allowing smooth 60fps rendering of multi-channel ECG waveforms and vitals without blocking the main UI thread.
- **Live Synthetic Data**: Includes a robust synthetic data generator that streams lifelike ADT (Admission, Discharge, Transfer) and HL7 v2/FHIR style metrics over WebSocket and polling mechanisms.

### 🧬 3. Federated Machine Learning Diagnostics
- **Edge-Based Predictions**: Predictive models (like XGBoost and Scikit-learn random forests) are embedded directly into the backend for instantaneous diagnostic probability scoring (e.g., cardiovascular risk trajectories).
- **Privacy-Preserving Architecture**: Designed to support federated learning nodes, allowing hospitals to train collaborative models without sharing raw patient PHI.

### ⚡ 4. Next-Generation Full-Stack Architecture
- **FastAPI Async Backend**: Python backend built entirely on `asyncio` for high concurrency, paired with SQLite (development) or PostgreSQL (production) for highly structured relational data.
- **React 19 & Vite**: The frontend is built on the bleeding edge of the React ecosystem using Vite for instant HMR (Hot Module Replacement) and optimized production builds.
- **Zustand State Management**: Lightweight, boilerplate-free global state management for seamlessly syncing UI components across the dashboard.

### 🔐 5. Enterprise-Grade Security
- **Strict CORS & Network Isolation**: Backend middleware rigorously validates Origin headers and Trusted Hosts, rejecting cross-site forgery attempts by default.
- **Offline Capable**: Features robust fallbacks and graceful degradation when external API connections (like internet-dependent services) are unavailable.
- **Rate Limiting**: Integrated `SlowAPI` throttling prevents DDOS and brute-force attacks at the application edge.

---

## 📸 Platform Screenshots

### 1. Secure Authentication Console
> *Zero-trust login interface featuring JWT encryption and active session auditing.*
<img src="docs/assets/screenshot-login.png" width="100%" alt="MedAssist AI Login Console" />

### 2. Clinical Operations Dashboard
> *The Nexus Vitalis command center for one-click patient care and hospital overviews.*
<img src="docs/assets/screenshot-dashboard.png" width="100%" alt="MedAssist AI Dashboard" />

### 3. Live Patient Telemetry
> *60fps OffscreenCanvas ECG rendering and real-time vitals monitoring for ICU beds.*
<img src="docs/assets/screenshot-telemetry.png" width="100%" alt="Live ECG Telemetry Grid" />

### 4. AI Clinical Copilot
> *HIPAA-compliant, localized AI querying for clinical decision support and medical guidelines.*
<img src="docs/assets/screenshot-copilot.png" width="100%" alt="MedAssist AI Copilot Interface" />

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.10+
- Node.js 18+
- [Ollama](https://ollama.ai) (Ensure `qwen2.5-coder:3b-8k` model is pulled)

### 2. Installation

Clone the repository and install dependencies for both ends:

```bash
git clone https://github.com/adarshgzz/MedAssist-AI.git
cd MedAssist-AI

# Install Python backend
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt

# Install Frontend
cd frontend
npm install
cd ..
```

### 3. Run the Platform

We have included a concurrent runner script to boot both the frontend and backend instantly:

```bash
# Activate your environment
source .venv/bin/activate

# Launch the stack
python run_servers.py
```

- **Frontend**: http://127.0.0.1:3000
- **Backend API**: http://127.0.0.1:8000

---

## 🛠 Technology Stack

### Frontend
- **Framework**: React 19 + TypeScript
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **Charts**: Recharts & Custom OffscreenCanvas API

### Backend
- **Framework**: FastAPI (Python)
- **AI Integration**: LangGraph & Ollama
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Machine Learning**: XGBoost, Scikit-learn, PyTorch

---

## 🤝 Contributing
Contributions, issues, and feature requests are highly welcome! Feel free to check the [issues page](https://github.com/adarshgzz/MedAssist-AI/issues).

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<div align="center">
  <i>Built with precision for the future of clinical AI.</i>
</div>
