import streamlit as st
import requests
from streamlit_lottie import st_lottie
from agent_researcher import search_the_web, get_content_from_urls, get_or_create_knowledge_base, get_answer_from_agent
from langchain_openai import OpenAIEmbeddings
import os

# --- Lottie Animasyon Yükleyici Fonksiyon ---
def load_lottie_url(url: str):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Hatalı durum kodları için bir istisna oluşturur
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"Lottie URL'i çekilirken hata oluştu: {e}")
        return None
    except ValueError: # JSONDecodeError'ı da kapsar
        print(f"URL'den gelen veri JSON formatında değil: {url}")
        return None

# --- Arayüz Ayarları ---
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

# --- Şifre Kontrolü ---
def check_password():
    try:
        password = st.text_input("Enter Password:", type="password")
        if not password: # İlk açılışta boş bırak
            st.info("Please enter the password to activate the assistant.")
            return False
        
        correct_password = st.secrets.get("APP_PASSWORD", "12345") # Lokal test için varsayılan şifre

        if password == correct_password:
            return True
        else:
            st.error("Incorrect password.")
            return False
    except Exception as e:
        st.error(f"An error occurred during password check: {e}")
        return False

if not check_password():
    st.stop()

st.success("Access Granted! Welcome to the AI Research Assistant.")
st.write("---")

# --- Lottie Animasyon Linkleri ---
lottie_thinking_url = "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
lottie_success_url = "https://assets10.lottiefiles.com/packages/lf20_xlpvdpe0.json"

# --- Kenar Çubuğu (Sidebar) ---
with st.sidebar:
    st.header("🔬 Research Controls")
    query = st.text_input(
        "Enter Research Topic:",
        placeholder="e.g., The future of AI in healthcare"
    )
    start_button = st.button("Start Research 🚀")

# --- Ana Sayfa ---
st.title("🤖 Autonomous AI Research Assistant")
st.markdown("Enter your research topic in the sidebar on the left and click 'Start Research' to generate a detailed, well-sourced report.")

if start_button:
    if not query:
        st.warning("Please enter a research topic in the sidebar.")
    else:
        lottie_thinking = load_lottie_url(lottie_thinking_url)
        
        with st.status("AI Agent is starting the mission...", expanded=True) as status:
            if lottie_thinking:
                st_lottie(lottie_thinking, speed=1, height=150, key="thinking")
            
            status.update(label="Step 1/4: Searching the web...")
            source_urls = search_the_web(query)
            if isinstance(source_urls, str):
                st.error(source_urls)
                st.stop()
            
            status.update(label=f"Step 2/4: Reading {len(source_urls)} sources...")
            documents = get_content_from_urls(source_urls)
            if not documents:
                st.error("Could not read content from sources.")
                st.stop()

            status.update(label="Step 3/4: Building AI knowledge base...")
            embeddings = OpenAIEmbeddings()
            knowledge_base = get_or_create_knowledge_base(documents, embeddings)
            
            status.update(label="Step 4/4: Writing the final report...")
            final_answer = get_answer_from_agent(query, knowledge_base)
            status.update(label="Research complete!", state="complete", expanded=False)

        st.success("Your report is ready!")
        lottie_success = load_lottie_url(lottie_success_url)
        if lottie_success:
            st_lottie(lottie_success, speed=1, loop=False, height=200, key="success")

        with st.expander("View Full AI-Generated Report", expanded=True):
            st.markdown(final_answer)