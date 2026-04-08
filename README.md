🌾 AgriBot: AI-Based Farmer Advisory Query System
AgriBot is a multilingual, AI-powered assistant developed to bridge the gap between complex agricultural science and local farming needs. By leveraging the Gemini 2.5 Flash model, it provides real-time crop advice, disease diagnosis, and localized guidance in multiple regional languages.

🚀 Key Features
Multilingual Interface: Supports Marathi (मराठी), Hindi (हिन्दी), and English to ensure accessibility for local farmers.

AI Disease Diagnosis: Farmers can upload photos of infected crop leaves; the system uses Computer Vision to identify diseases and suggest organic or chemical treatments.

Hybrid Knowledge Base: Combines a localized knowledge_base.txt (for region-specific soil and crop data) with general AI intelligence for broad agricultural queries.

User-Friendly UI: Built with Streamlit, offering a clean, chat-based experience that works on both mobile and desktop.

🛠️ Tech Stack
Core Logic: Python 3.11+

Frontend: Streamlit

AI Engine: Google Gemini 2.5 Flash API

Version Control: Git & GitHub

Farmer_AI_Project/
├── main.py                # Main Application Logic
├── knowledge_base.txt      # Local Agricultural Data
├── .env                   # API Keys (Protected via .gitignore)
├── requirements.txt       # Project Dependencies
└── README.md              # Project Documentation
⚙️ Installation & Setup
Clone the Repository:

Bash
git clone https://github.com/MinakshiGadpalli/AgriBot-Farmer-Advisory-System.git
cd AgriBot-Farmer-Advisory-System
Install Dependencies:

Bash
pip install -r requirements.txt
Configure API Key:
Create a .env file in the root directory and add your API key:

Plaintext
GOOGLE_API_KEY=your_api_key_here
Run the Application:

Bash
streamlit run main.py
