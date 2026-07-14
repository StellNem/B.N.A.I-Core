# 📡 B.N.A.I Core — Local AI Agent Template

A lightweight, production-ready local AI agent boilerplate built with **Streamlit** and **Ollama (Qwen 2.5 / Llama 3)**. Run 100% private, offline AI agents on standard laptop hardware with zero API cloud fees.

---

## ⚡ Get the Full Production Architecture
This repository contains the foundational setup. The complete, production-ready **B.N.A.I Core** system—featuring automatic port management, offline-to-online web search tools, and dual-layer JSON memory—is available on Gumroad.

👉 **[Download the Production-Ready Boilerplate on Gumroad](https://stellnem.gumroad.com/l/ayjaeo)**

---

## ✨ Features (Full Version)

*   **Zero-Config Launcher (`ignite.py`):** Automatically sweeps local ports, terminates dangling ghost processes, and wakes up the Ollama daemon before launching the UI.
*   **Dual-Layer Memory:** Silently archives full raw conversations on disk while summarizing key interactions into a tiny context cache to protect your laptop's VRAM.
*   **Smart Native Tool Calling:** Detects when real-time information is needed and triggers Tavily search tools directly through your local Ollama client.
*   **Responsive UI:** A clean, dark-mode Streamlit dashboard designed for fast, local developer workflows.

---

## 🚀 Quick Start (Foundational Setup)

### 1. Prerequisites
Ensure you have Python 3.9+ and Ollama installed. Download your preferred local model:
```bash
ollama pull qwen2.5:7b
