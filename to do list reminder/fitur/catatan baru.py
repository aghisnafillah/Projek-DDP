import streamlit as st
import datetime

# Tambahkan gambar header dengan ukuran dan kotak
st.markdown(
    """
    <style>
    .header-image {
        width: 60%;
        max-width: 300px;
        margin: 0 auto;
        border: 2px solid #ccc;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="https://cf-sparkai-live.s3.amazonaws.com/users/2qylvW8QEl51jk0ptMuOWAl23HP/spark_ai/o_bg-remover-gen_2qym6qLBjmAI00FMTpaeKKkleHd.png" alt="Header Image" class="header-image">
        <p>Selamat Menuliskan curahan Hati anda 📝</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Fungsi untuk menambahkan data ke riwayat
if "history" not in st.session_state:
    st.session_state["history"] = []
def add_to_history(entry_type, entry_data):
    st.session_state["history"].append({"Jenis": entry_type, "Data": entry_data})

if "catatan" not in st.session_state:
    st.session_state["catatan"] = []

# Halaman Catatan Baru
st.subheader("📝 Buat Catatan Baru")
with st.form("form_catatan"):
    date = st.date_input("📅 Tanggal", datetime.datetime.today().date())
    judul = st.text_input("📓 Judul Catatan", "")
    isi = st.text_area("✍️ Isi Catatan", "")
    simpan = st.form_submit_button("✅ Simpan Catatan")

if simpan:
    if judul.strip() == "" or isi.strip() == "":
        st.error("❌ Judul dan isi catatan tidak boleh kosong.")
    else:
        entry = {"Tanggal": date, "Judul": judul, "Isi": isi}
        st.session_state["catatan"].append(entry)
        add_to_history("Catatan Baru", entry)
        st.success("✔️ Catatan berhasil disimpan.")

# Tampilkan catatan tersimpan
st.subheader("📚 Catatan Tersimpan")
if st.session_state["catatan"]:
    for i, catatan in enumerate(list(st.session_state["catatan"])):
        with st.expander(f"📓 {catatan['Judul']} ({catatan['Tanggal']})"):
            st.write(catatan["Isi"])
            if st.button(f"🗑️ Hapus Catatan {i+1}", key=f"hapus_{i}"):
                del st.session_state["catatan"][i]
                st.success("✔️ Catatan berhasil dihapus.")
else:
    st.info("ℹ️ Belum ada catatan yang tersimpan.")
