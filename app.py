import streamlit as st
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db

# Inisialisasi Firebase
@st.cache_resource
def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(r"C:\Users\dell\Downloads\cloud-computing-1ce46-firebase-adminsdk-fbsvc-b3af253433.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://cloud-computing-1ce46-default-rtdb.asia-southeast1.firebasedatabase.app'
        })
    return db

# Fungsi menyimpan absensi
def simpan_absensi(nama):
    firebase_db = init_firebase()
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ref = firebase_db.reference('absensi')
    ref.push({
        'nama': nama,
        'waktu': waktu,
        'status': 'Hadir'
    })
    return waktu

# Fungsi menyimpan pegawai
def simpan_pegawai(nip, nama, jabatan):
    firebase_db = init_firebase()
    ref = firebase_db.reference(f'pegawai/{nip}')
    ref.set({
        'nip': nip,
        'nama': nama,
        'jabatan': jabatan
    })

# ==================== UI Streamlit ====================

st.set_page_config(page_title="Absensi & Pegawai", layout="centered")
st.title("Aplikasi Absensi dan Data Pegawai")

# Navigasi antar fitur
menu = st.sidebar.selectbox("Pilih Halaman", ["Beranda", "Absensi", "Input Data Pegawai"])

# ==================== Halaman Beranda ====================
if menu == "Beranda":
    st.subheader("Selamat datang!")
    st.write("Gunakan menu di samping untuk melakukan absensi atau input data pegawai.")

# ==================== Halaman Absensi ====================
elif menu == "Absensi":
    st.subheader("Form Absensi")
    nama = st.text_input("Masukkan Nama")

    if st.button("Absen"):
        if nama.strip():
            waktu = simpan_absensi(nama)
            st.success(f"{nama} berhasil absen pada {waktu}")
        else:
            st.warning("Nama tidak boleh kosong.")

# ==================== Halaman Input Data Pegawai ====================
elif menu == "Input Data Pegawai":
    st.subheader("Form Input Pegawai")
    nip = st.text_input("NIP")
    nama = st.text_input("Nama")
    jabatan = st.text_input("Jabatan")

    if st.button("Simpan Pegawai"):
        if nip.strip() and nama.strip() and jabatan.strip():
            simpan_pegawai(nip, nama, jabatan)
            st.success(f"Data pegawai {nama} berhasil disimpan.")
        else:
            st.warning("Semua kolom harus diisi.")
