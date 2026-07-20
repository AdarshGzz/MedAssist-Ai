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

## ✨ Features

- **🧠 Local AI Copilot**: Powered by local inference (e.g., Qwen 2.5) via Ollama. No data leaves your machine.
- **📈 Real-Time Vitals**: High-performance OffscreenCanvas ECG monitoring with synthetic real-time data streaming.
- **🔐 Enterprise Security**: Offline-first design, strict CORS, rate limiting, and zero-trust authentication.
- **⚡ Ultra-Fast Stack**: Vite + React 19 frontend paired with a FastAPI async backend.
- **🧬 Federated Learning**: Edge-based machine learning models built for privacy-preserving clinical diagnostics.

---

## 📸 Platform Screenshots

### Clinical Dashboard
> *Live monitoring of patient vitals and predictive diagnostics.*
<img src="docs/assets/screenshot-dashboard.png" width="100%" alt="MedAssist AI Dashboard" />

### AI Copilot Interface
> *HIPAA-compliant, localized AI querying for clinical decision support.*
<img src="docs/assets/screenshot-copilot.png" width="100%" alt="MedAssist AI Copilot" />

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
