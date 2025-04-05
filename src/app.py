import streamlit as st
import os
from dotenv import load_dotenv
from agents import DenizAgent, PolatAgent, KararsizAgent
import time
from typing import List, Dict

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Tartışma Simülasyonu",
    page_icon="🗣️",
    layout="wide"
)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'simulation_running' not in st.session_state:
    st.session_state.simulation_running = False
if 'agents' not in st.session_state:
    st.session_state.agents = {
        'deniz': DenizAgent(),
        'polat': PolatAgent(),
        'kararsiz': KararsizAgent()
    }
if 'analysis_shown' not in st.session_state:
    st.session_state.analysis_shown = False
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'current_conversation_id' not in st.session_state:
    st.session_state.current_conversation_id = 0

# Sidebar
with st.sidebar:
    st.header("📝 Gündem Özeti")
    agenda = st.text_area(
        "Tartışılacak konuyu özetleyin:",
        height=150,
        placeholder="Örnek: Türkiye'de son zamanlarda artan enflasyon ve ekonomik politikalar hakkında..."
    )
    
    if st.button("🚀 Simülasyonu Başlat", disabled=not agenda):
        st.session_state.simulation_running = True
        st.session_state.messages = []  # Mesajları temizle
        st.session_state.analysis_shown = False
    
    if st.button("🛑 Simülasyonu Durdur", disabled=not st.session_state.simulation_running):
        st.session_state.simulation_running = False
    
    # Yeni konuşma ve konuşmayı silme butonları
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🆕 Yeni Konuşma"):
            # Mevcut konuşmayı geçmişe kaydet
            if st.session_state.messages:
                st.session_state.conversation_history.append({
                    "id": st.session_state.current_conversation_id,
                    "agenda": agenda,
                    "messages": st.session_state.messages.copy()
                })
                st.session_state.current_conversation_id += 1
            
            # Yeni konuşma için hazırla
            st.session_state.messages = []
            st.session_state.simulation_running = False
            st.session_state.analysis_shown = False
            st.rerun()
    
    with col2:
        if st.button("🗑️ Konuşmayı Sil"):
            st.session_state.messages = []
            st.rerun()
    
    # Konuşma geçmişi
    st.markdown("---")
    st.header("📚 Konuşma Geçmişi")
    
    if st.session_state.conversation_history:
        for conv in reversed(st.session_state.conversation_history):
            with st.expander(f"Konuşma #{conv['id']+1}: {conv['agenda'][:30]}..."):
                for msg in conv['messages']:
                    if msg['role'] == 'Deniz':
                        st.markdown(f"**Deniz (CHP):** {msg['content']}")
                    elif msg['role'] == 'Polat':
                        st.markdown(f"**Polat (AKP):** {msg['content']}")
                    elif msg['role'] == 'Kararsız-Küskün Seçmen':
                        st.markdown(f"**Miraç (Kararsız-Küskün Seçmen):** {msg['content']}")
    else:
        st.info("Henüz kaydedilmiş konuşma yok.")

# Main content
st.title("🗣️ Siyasi Tartışma Simülasyonu")
st.markdown("""
Bu uygulama, verilen bir gündem özeti üzerinde iki farklı siyasi görüşe sahip yapay zeka ajanının tartışmasını simüle eder.
* 🟥 **Deniz** (CHP): Aydın, kültürlü, entelektüel
* 🟦 **Polat** (AKP): Muhafazakar, taşralı, halkçı
* 🟨 **Miraç (Kararsız-Küskün Seçmen)**: Sorgulayıcı ve memnuniyetsiz, muhafazakar ve milliyetçi bir aileden gelen seküler yaşam tarzı süren
""")

# Tartışma alanı
if st.session_state.messages:
    for msg in st.session_state.messages:
        if msg['role'] == 'Deniz':
            with st.chat_message("user", avatar="🟥"):
                st.markdown(f"**Deniz (CHP):** {msg['content']}")
        elif msg['role'] == 'Polat':
            with st.chat_message("assistant", avatar="🟦"):
                st.markdown(f"**Polat (AKP):** {msg['content']}")
        elif msg['role'] == 'Kararsız-Küskün Seçmen':
            with st.chat_message("user", avatar="🟨"):
                st.markdown(f"**Miraç (Kararsız-Küskün Seçmen):** {msg['content']}")

# Simülasyon durdurulduğunda ve analiz gösterilmediğinde
if not st.session_state.simulation_running and st.session_state.messages and not st.session_state.analysis_shown:
    st.markdown("---")
    st.subheader("📊 Kararsız-Küskün Seçmen Analizi")
    
    analysis = st.session_state.agents['kararsiz'].analyze_debate(agenda, st.session_state.messages)
    st.session_state.messages.append({"role": "Kararsız-Küskün Seçmen", "content": analysis})
    st.session_state.analysis_shown = True
    st.rerun()
    
# Simülasyon mantığı
if st.session_state.simulation_running and agenda:
    # İlk konuşmacı Deniz (CHP)
    if not st.session_state.messages:
        response = st.session_state.agents['deniz'].generate_response(agenda, [])
        st.session_state.messages.append({"role": "Deniz", "content": response})
        time.sleep(1)
        st.rerun()
    
    # Sırayla konuşma
    last_speaker = st.session_state.messages[-1]['role']
    if last_speaker == "Deniz":
        response = st.session_state.agents['polat'].generate_response(agenda, st.session_state.messages)
        st.session_state.messages.append({"role": "Polat", "content": response})
    else:
        response = st.session_state.agents['deniz'].generate_response(agenda, st.session_state.messages)
        st.session_state.messages.append({"role": "Deniz", "content": response})
    
    time.sleep(1)
    st.rerun() 