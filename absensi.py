import streamlit as st
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db

# Inisialisasi Firebase hanya sekali
@st.cache_resource
def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("cloud-computing-1ce46-firebase-adminsdk-fbsvc-7379355383.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://cloud-computing-1ce46-default-rtdb.asia-southeast1.firebasedatabase.app'
        })
    return db

# Fungsi untuk menyimpan absensi ke Firebase
def simpan_absensi(nama):
    firebase_db = init_firebase()  # pastikan Firebase sudah inisialisasi
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ref = firebase_db.reference('absensi')
    ref.push({
        'nama': nama,
        'waktu': waktu,
        'status': 'Hadir'
    })
    return waktu

# UI Streamlit
st.title("Aplikasi Absensi")

nama = st.text_input("Masukkan nama")

if st.button("Absen"):
    if nama.strip() != "":
        waktu_absen = simpan_absensi(nama)
        st.success(f"Absensi berhasil pada {waktu_absen}")
    else:
        st.warning("Nama tidak boleh kosong.")
