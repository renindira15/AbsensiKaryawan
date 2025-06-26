import streamlit as st
import firebase_admin
from firebase_admin import credentials, db

# Fungsi untuk inisialisasi Firebase
@st.cache_resource  # agar tidak diinisialisasi berulang setiap rerun
def init_firebase():
    if not firebase_admin._apps:  # hanya inisialisasi jika belum dilakukan
        cred = credentials.Certificate(r"C:\Users\dell\Downloads\cloud-computing-1ce46-firebase-adminsdk-fbsvc-b3af253433.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://cloud-computing-1ce46-default-rtdb.asia-southeast1.firebasedatabase.app'
        })
    return db

# Contoh penggunaan
firebase_db = init_firebase()

# Misalnya: ambil data dari path tertentu
ref = firebase_db.reference('path_data')
data = ref.get()

st.write("Data dari Firebase:", data)
