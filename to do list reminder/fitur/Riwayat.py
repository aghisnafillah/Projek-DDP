import streamlit as st
import pandas as pd

# Inisialisasi session state untuk data dan riwayat
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame(columns=["Tanggal", "Kategori", "Tipe", "Jumlah"])
if "history" not in st.session_state:
    st.session_state["history"] = []

# Header Riwayat
st.markdown("<h2 style='text-align: center; color: #2c3e50;'>📜 Riwayat</h2>", unsafe_allow_html=True)

# Bagian riwayat
if st.session_state["history"]:
    st.markdown("<div style='margin-bottom: 20px; text-align: center;'>Berikut adalah daftar riwayat Anda:</div>", unsafe_allow_html=True)

    for idx, entry in enumerate(st.session_state["history"]):
        with st.expander(f"{idx+1}. {entry['Jenis']}", expanded=False):
            st.markdown("<div style='padding: 10px; background-color: #ecf0f1; border-radius: 5px;'>", unsafe_allow_html=True)
            st.write(entry["Data"])
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Tombol hapus riwayat
    if st.button("🗑 Hapus Semua Riwayat", use_container_width=True):
        st.session_state["history"] = []
        st.success("Riwayat berhasil dihapus.")
else:
    st.markdown("<div style='text-align: center; color: #e74c3c;'>⚠ Belum ada riwayat yang tersedia.</div>", unsafe_allow_html=True)