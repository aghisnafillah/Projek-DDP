
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Fungsi untuk menambahkan data ke riwayat
if "history" not in st.session_state:
    st.session_state["history"] = []

def add_to_history(entry_type, entry_data):
    st.session_state["history"].append({"Jenis": entry_type, "Data": entry_data})

# Inisialisasi session_state
if "saldo_utama" not in st.session_state:
    st.session_state.saldo_utama = 0

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Tanggal", "Kategori", "Tipe", "Jumlah"])

# Judul aplikasi dengan emoji dan gambar
st.title("💸 Pengelolaan Keuangan")
st.image("https://cf-sparkai-live.s3.amazonaws.com/users/2qylvW8QEl51jk0ptMuOWAl23HP/spark_ai/o_bg-remover-gen_2qzCi0kx18QLAoI6BFVxr7oospc.png", width=300)
st.markdown("**Kelola keuangan Anda dengan lebih cerdas dan rapi!**")

# Subheader saldo utama dengan emoji
st.subheader("💼 Saldo Utama")

# Form untuk memasukkan saldo utama
data_style = "font-size:20px; font-family: 'Arial'; color: green;"
with st.form("form_keuangan"):
    if st.session_state.saldo_utama == 0:
        saldo_utama_input = st.number_input(
            "💰 Masukkan saldo utama Anda (Rp)", 
            min_value=0, 
            step=1000, 
            format="%d"
        )
    else:
        st.markdown(f"<div style='{data_style}'>Saldo utama Anda: <b>Rp {st.session_state.saldo_utama:,.2f}</b></div>", unsafe_allow_html=True)

    submit = st.form_submit_button("✔️ Simpan saldo utama")

    if submit and st.session_state.saldo_utama == 0:
        st.session_state.saldo_utama = saldo_utama_input
        st.success(f"Saldo utama sebesar Rp {saldo_utama_input:,.2f} berhasil disimpan! 🥳")

# Pilihan rentang waktu dengan emoji
pilihan_waktu = st.selectbox("📆 Pilih rentang waktu:", ["Harian", "Mingguan", "Bulanan"])

# Form untuk input transaksi
st.subheader("📝 Masukkan Transaksi")
with st.form("input_form"):
    tanggal = st.date_input("📅 Tanggal")
    kategori = st.text_input("📂 Kategori (contoh: Makanan, Gaji, dll.)")
    tipe = st.radio("📈 Tipe", ["Pemasukan", "Pengeluaran"], horizontal=True)
    jumlah = st.number_input("💵 Jumlah", min_value=0, step=1000)
    submit = st.form_submit_button("➕ Tambah")

if submit:
    new_data = pd.DataFrame([[tanggal, kategori, tipe, jumlah]],
                            columns=["Tanggal", "Kategori", "Tipe", "Jumlah"])
    st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
    st.success("Data berhasil ditambahkan! ✅")

    add_to_history("Transaksi Keuangan", {
        "Tanggal": tanggal,
        "Kategori": kategori,
        "Tipe": tipe,
        "Jumlah": jumlah})

    today = datetime.now().date()

    if pilihan_waktu == "Harian":
        pengeluaran_harian = st.session_state.data[
            (st.session_state.data["Tipe"] == "Pengeluaran") &
            (st.session_state.data["Tanggal"] == today)
        ]
        total_pengeluaran_harian = pengeluaran_harian["Jumlah"].sum()

        st.markdown(f"### 🎯 Total Pengeluaran Hari Ini: Rp {total_pengeluaran_harian:,.2f}")
        if total_pengeluaran_harian > 100000:
            st.warning("⚠️ Pengeluaran harian Anda lebih dari Rp 100,000. Anda termasuk boros!")
        else:
            st.success("🎉 Pengeluaran Anda di bawah Rp 100,000. Anda hebat!")

    elif pilihan_waktu == "Mingguan":
        one_week_ago = today - timedelta(days=7)
        pengeluaran_mingguan = st.session_state.data[
            (st.session_state.data["Tipe"] == "Pengeluaran") &
            (st.session_state.data["Tanggal"] >= one_week_ago)
        ]
        total_pengeluaran_mingguan = pengeluaran_mingguan["Jumlah"].sum()

        st.markdown(f"### 📅 Total Pengeluaran Minggu Ini: Rp {total_pengeluaran_mingguan:,.2f}")
        if total_pengeluaran_mingguan > 500000:
            st.warning("⚠️ Pengeluaran Anda lebih dari Rp 500,000. Anda termasuk boros!")
        else:
            st.success("👍 Pengeluaran Anda di bawah Rp 500,000. Anda hebat!")

    elif pilihan_waktu == "Bulanan":
        one_month_ago = today - timedelta(days=30)
        pengeluaran_bulanan = st.session_state.data[
            (st.session_state.data["Tipe"] == "Pengeluaran") &
            (st.session_state.data["Tanggal"] >= one_month_ago)
        ]
        total_pengeluaran_bulanan = pengeluaran_bulanan["Jumlah"].sum()

        st.markdown(f"### 📅 Total Pengeluaran Bulan Ini: Rp {total_pengeluaran_bulanan:,.2f}")
        if total_pengeluaran_bulanan > 15000000:
            st.warning("⚠️ Pengeluaran bulanan Anda lebih dari Rp 15,000,000. Anda mungkin boros.")
        else:
            st.success("💪 Pengeluaran Anda di bawah Rp 15,000,000. Anda hebat!")

# Tampilkan data dan total saldo dengan tabel bergaya
st.markdown("### 📋 Riwayat Transaksi")
st.dataframe(st.session_state.data.style.format(subset=["Jumlah"], formatter="Rp {:,.2f}"))

# Menampilkan total saldo dengan tabel bergaya
st.markdown("### 🏦 Total Saldo")
total_pemasukan = st.session_state.data[st.session_state.data["Tipe"] == "Pemasukan"]["Jumlah"].sum()
total_pengeluaran = st.session_state.data[st.session_state.data["Tipe"] == "Pengeluaran"]["Jumlah"].sum()
saldo = st.session_state.saldo_utama + total_pemasukan - total_pengeluaran

saldo_data = pd.DataFrame({
    "Saldo Utama": [f"Rp {st.session_state.saldo_utama:,.2f}"],
    "Total Pemasukan": [f"Rp {total_pemasukan:,.2f}"],
    "Total Pengeluaran": [f"Rp {total_pengeluaran:,.2f}"],
    "Saldo Akhir": [f"Rp {saldo:,.2f}"]
})

st.table(saldo_data.style.set_properties(**{"font-size": "18px", "text-align": "center"}))
