import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
from dotenv import load_dotenv

# 1. Setup
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    # Using the stable 2.5 flash model which supports both text and images
    model = genai.GenerativeModel('gemini-2.5-flash') 
else:
    st.error("API Key not found! Please check your .env file.")

# 2. UI Styling
st.set_page_config(page_title="AgriBot Pro", page_icon="🌾", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #2e7d32; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌾 AgriBot: AI Farmer Advisory & Disease Detection")

# 3. Sidebar for Image Upload (Project Requirement)
st.sidebar.header("📸 Disease Diagnosis")
uploaded_file = st.sidebar.file_uploader("Upload a photo of the infected plant/leaf", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.sidebar.image(image, caption="Uploaded Image", use_container_width=True)
    
    if st.sidebar.button("Analyze Image"):
        with st.spinner("Analyzing plant health..."):
            # Prompt for image analysis
            analysis_prompt = "Identify the plant and any visible diseases or pests. Provide organic and chemical treatment suggestions for a farmer."
            response = model.generate_content([analysis_prompt, image])
            
            st.subheader("📋 Disease Analysis Report")
            st.info(response.text)

# 4. Main Chat Interface
st.divider()
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! Ask me a farming question or upload a photo in the sidebar for disease detection."}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question (e.g., How much urea for 1 acre of wheat?)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Read local knowledge base
            context = ""
            if os.path.exists("knowledge_base.txt"):
                with open("knowledge_base.txt", "r") as f:
                    context = f.read()

            full_prompt = f"Context: {context}\n\nQuestion: {prompt}"
            response = model.generate_content(full_prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {e}")