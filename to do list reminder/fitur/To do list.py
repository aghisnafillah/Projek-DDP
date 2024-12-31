import streamlit as st
from datetime import time
import pandas as pd

# Fungsi untuk menambahkan data ke riwayat
if "history" not in st.session_state:
    st.session_state["history"] = []
def add_to_history(entry_type, entry_data):
    st.session_state["history"].append({"Jenis": entry_type, "Data": entry_data})

# Inisialisasi session state
if "jadwal" not in st.session_state:
    st.session_state.jadwal = []

# Fungsi untuk memperbarui status aktivitas
def update_status(index):
    st.session_state.jadwal[index]["Selesai"] = not st.session_state.jadwal[index]["Selesai"]


# Tambahkan CSS untuk estetika
st.markdown(
    """
    <style>
    .header {
        text-align: center;
        color: #213555;
        margin-bottom: 20px;
    }
    .form-container {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .table-container {
        margin-top: 20px;
    }
    .stButton > button {
        background-color: #3E5879;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #F5EFE7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Halaman To Do List
st.markdown("<h2 class='header'>🔖 To Do List</h2>", unsafe_allow_html=True)
st.image("https://cf-sparkai-live.s3.amazonaws.com/users/2qylvW8QEl51jk0ptMuOWAl23HP/spark_ai/o_bg-remover-gen_2qzEMPK3dS09fmAmcZ1JYsFqK5l.png", width=300)
# Form untuk menambahkan aktivitas
st.markdown("<div class='form-container'>", unsafe_allow_html=True)
with st.form("form_aktivitas"):
    aktivitas = st.text_input("✍️ Nama Aktivitas", "")
    waktu_mulai = st.time_input("⏰ Waktu Mulai", value=time())
    waktu_selesai = st.time_input("⏳ Waktu Selesai", value=time())
    submit = st.form_submit_button("➕ Tambahkan")
st.markdown("</div>", unsafe_allow_html=True)

# Tambahkan aktivitas ke jadwal
if submit:
    if waktu_mulai >= waktu_selesai:
        st.error("Waktu mulai harus lebih awal dari waktu selesai.")
    elif aktivitas.strip() == "":
        st.error("Nama aktivitas tidak boleh kosong.")
    else:
        entry = {
            "Aktivitas": aktivitas,
            "Waktu Mulai": waktu_mulai.strftime("%H:%M"),
            "Waktu Selesai": waktu_selesai.strftime("%H:%M"),
            "Selesai": False
        }
        st.session_state.jadwal.append(entry)
        add_to_history("To Do List", entry)
        st.success("Aktivitas berhasil ditambahkan.")

# Tampilkan jadwal
if st.session_state.jadwal:
    st.markdown("<div class='table-container'>", unsafe_allow_html=True)
    for i, item in enumerate(st.session_state.jadwal):
        col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
        with col1:
            st.markdown(f"📝 **{item['Aktivitas']}**")
        with col2:
            st.markdown(f"⏰ {item['Waktu Mulai']}")
        with col3:
            st.markdown(f"⏳ {item['Waktu Selesai']}")
        with col4:
            st.checkbox(
                "✔️ Selesai",
                value=item["Selesai"],
                key=f"checkbox_{i}",
                on_change=update_status,
                args=(i,)
            )
    st.markdown("</div>", unsafe_allow_html=True)

# Tampilkan jadwal dalam bentuk tabel
if st.session_state.jadwal:
    # Mengonversi daftar aktivitas ke DataFrame
    data_jadwal = pd.DataFrame(st.session_state.jadwal)
    data_jadwal["Selesai"] = data_jadwal["Selesai"].map({True: "✔️", False: "❌"})  # Mengubah status selesai jadi ikon

    # Menampilkan tabel
    st.markdown("<div class='table-container'>", unsafe_allow_html=True)
    st.table(data_jadwal)  # Untuk tabel statis
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("Belum ada aktivitas pada jadwal hari ini.")

# Tombol untuk reset jadwal
if st.button("🗑️ Reset Jadwal"):
    st.session_state.jadwal = []
    st.success("Jadwal telah direset.")
