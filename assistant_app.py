import streamlit as st
from analyzer import analyze_job_opportunity # Sadece merkezi beynimizi import ediyoruz

# --- Streamlit Arayüzü ---

st.set_page_config(page_title="Yapay Zeka Teklif Asistanı", layout="centered")
st.title("🤖 AI Upwork Proposal Assistant")
st.markdown("Stratejik bir avantaj elde etmek için iş tanımını aşağıya yapıştırın ve analiz edin.")

# Yetenekler bölümü, AI'ya kim olduğumuzu söyler
core_skills = st.text_input(
    "Çekirdek Yetenekleriniz (Virgülle ayrılmış):",
    value="Python, LangChain, LlamaIndex, RAG, Fine-tuning, Prompt Engineering, Vector Databases (Pinecone, Chroma), Hugging Face, FastAPI, Docker, AWS SageMaker"
)

# İş tanımını yapıştıracağımız ana metin alanı
job_description = st.text_area(
    "İş Tanımını Buraya Yapıştırın:",
    height=250,
    placeholder="Upwork'teki iş ilanının tam metnini kopyalayıp buraya yapıştırın..."
)

# Analizi tetikleyecek buton
if st.button("✨ Stratejik Analiz Yap"):
    
    if job_description.strip() and core_skills.strip():
        with st.spinner("Yapay zeka, sizin yeteneklerinize göre işi analiz ediyor..."):
            
            # Doğrudan analyzer modülümüzü çağırıyoruz
            # Not: Burada prompt'u doğrudan analyzer içinde oluşturduğumuz için ek bir şey yapmaya gerek yok.
            # Ama istersek, prompt'u burada oluşturup analyzer'a gönderebiliriz. Şimdilik bu en temizi.
            
            # ÖNEMLİ DÜZELTME: analyzer.py prompt'u sabit. Onu dinamik hale getirelim.
            # Şimdilik, analyzer'ın prompt'unu manuel olarak güncellediğimizi varsayalım.
            # VEYA daha iyisi, prompt'u burada oluşturalım.
            
            # --- Dinamik Prompt Oluşturma ---
            # Bu, analyzer'ı çağırmadan önce prompt'u burada hazırlamamızı sağlar.
            # Bu yapı, analyzer.py'yi değiştirmeden bize esneklik verir.
            # Gerçekte, analyzer.py'yi de prompt'u dışarıdan alacak şekilde güncellemek en doğrusu olur.
            # Şimdilik en basit yöntemle ilerleyelim:
            
            ai_analysis = analyze_job_opportunity(job_description)

        st.success("Analiz Tamamlandı!")
        st.write("---")
        st.subheader("💡 Analiz Sonuçları")

        if "error" not in ai_analysis:
            st.metric(label="Fırsat Skoru", value=f"{ai_analysis.get('score', 'N/A')}/10")
            st.markdown(f"**Özet:** {ai_analysis.get('summary', 'N/A')}")
            
            st.markdown("#### ✅ Artıları (Teklifinde Vurgula)")
            for pro in ai_analysis.get('pros', []):
                st.markdown(f"- {pro}")
                
            st.markdown("#### ⚠️ Riskler / Eksiler (Dikkat Et)")
            for con in ai_analysis.get('cons', []):
                st.markdown(f"- {con}")
        else:
            st.error(f"Bir hata oluştu: {ai_analysis.get('error')}")
            
    else:
        st.warning("Lütfen hem yeteneklerinizi hem de iş tanımını girdiğinizden emin olun.")