# 🚀 Vendor Intelligence Dashboard

An AI-powered system for detecting duplicate vendors, estimating cost savings, and generating actionable business insights.

---

## 📌 Project Overview

Vendor duplication is a major challenge in enterprise procurement systems, leading to redundant contracts, inefficiencies, and increased costs.

This project provides an intelligent solution that:

- Detects duplicate vendors using fuzzy matching
- Estimates potential cost savings
- Generates AI-based insights
- Allows interactive Q&A using LLaMA-based models

---

## 🎯 Key Features

✅ Duplicate Vendor Detection (RapidFuzz)  
✅ Cost Savings Analysis  
✅ Interactive Dashboard (Django + Tailwind)  
✅ AI-powered Insights (LLaMA / FLAN-T5)  
✅ Ask AI Feature (Context-based Q&A)  
✅ CSV Upload Support  
✅ Data Visualization (Matplotlib)  

---

## 🧠 AI & Models Used

| Component | Model/Technique |
|----------|----------------|
| Duplicate Detection | RapidFuzz (Fuzzy Matching) |
| AI Insights | Rule-based + LLM |
| LLM (Local AI) | distilgpt2 / flan-t5-base |
| NLP | Prompt Engineering |

---

## 🏗️ System Architecture


User Upload CSV
↓
Data Preprocessing
↓
Duplicate Detection (RapidFuzz)
↓
Savings Calculation
↓
AI Report Generation
↓
Dashboard Visualization
↓
Ask AI (LLaMA-based Q&A)


---

## 📊 Sample Outputs

- Duplicate vendor pairs
- Estimated savings (₹)
- AI-generated executive summary
- Interactive Q&A responses

---

## ⚙️ Tech Stack

- Python 🐍
- Django 🌐
- RapidFuzz 🔍
- Transformers (HuggingFace) 🤖
- Matplotlib 📊
- HTML + Tailwind CSS 🎨

---

## 📂 Project Structure


vendor_ai/
│
├── vendor_ai/ # Django project
├── vendors/ # Main app
│ ├── views.py
│ ├── utils.py
│ ├── ai_utils.py
│ ├── templates/
│
├── media/ # Generated charts
├── manage.py


---

## 🚀 How to Run

### 1. Clone Repository


git clone https://github.com/BharkaviPM/Vendor_AI.git
cd Vendor_AI

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run Server
python manage.py runserver

### 5. Open in Browser
http://127.0.0.1:8000/

### 📈 Innovation
Combines data analytics + AI + LLM
Provides end-to-end enterprise workflow
Enables interactive decision-making
Uses local LLM (offline AI capability)

### 🔮 Future Improvements
Integration with real procurement systems
Advanced ML models for anomaly detection
Deployment on cloud (AWS/GCP)
Real-time vendor monitoring

### 👩‍💻 Author

Bharkavi PM

### ⭐ Acknowledgements
HuggingFace Transformers
RapidFuzz
Django Framework

---

# 🚀 NOW PUSH README

Run:

git add README.md
git commit -m "Added professional README"
git push origin main --force
