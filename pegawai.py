import streamlit as st
import firebase_admin
from firebase_admin import credentials, db

# Inisialisasi Firebase sekali saja
@st.cache_resource
def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("cloud-computing-1ce46-firebase-adminsdk-fbsvc-7379355383.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://cloud-computing-1ce46-default-rtdb.asia-southeast1.firebasedatabase.app'
        })
    return db

# Fungsi untuk menyimpan data pegawai
def simpan_pegawai(nip, nama, jabatan):
    firebase_db = init_firebase()
    ref = firebase_db.reference(f'pegawai/{nip}')
    ref.set({
        'nip': nip,
        'nama': nama,
        'jabatan': jabatan
    })

# Antarmuka pengguna Streamlit
st.title("Form Input Pegawai")

nip = st.text_input("NIP")
nama = st.text_input("Nama")
jabatan = st.text_input("Jabatan")

if st.button("Simpan Pegawai"):
    if nip.strip() and nama.strip() and jabatan.strip():
        simpan_pegawai(nip, nama, jabatan)
        st.success(f"Data pegawai {nama} berhasil disimpan.")
    else:
        st.warning("Semua kolom harus diisi.")
