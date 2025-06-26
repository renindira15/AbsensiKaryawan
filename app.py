import streamlit as st
from absensi import simpan_absensi
from pegawai import simpan_pegawai

st.set_page_config(page_title="Absensi Karyawan", layout="centered")

st.title("Aplikasi Absensi dan Data Pegawai")

menu = st.sidebar.selectbox("Pilih Halaman", ["Beranda", "Absensi", "Input Data Pegawai"])

if menu == "Beranda":
    st.subheader("Selamat Datang di Aplikasi Absensi")
    st.write("Gunakan menu di samping untuk mulai.")

elif menu == "Absensi":
    st.subheader("Form Absensi")
    nama = st.text_input("Nama Karyawan")
    if st.button("Absen"):
        if nama.strip():
            waktu = simpan_absensi(nama)
            st.success(f"{nama} berhasil absen pada {waktu}")
        else:
            st.warning("Nama tidak boleh kosong.")

elif menu == "Input Data Pegawai":
    st.subheader("Form Input Data Pegawai")
    nip = st.text_input("NIP")
    nama = st.text_input("Nama")
    jabatan = st.text_input("Jabatan")
    if st.button("Simpan"):
        if nip and nama and jabatan:
            simpan_pegawai(nip, nama, jabatan)
            st.success(f"Data pegawai {nama} berhasil disimpan.")
        else:
            st.warning("Semua kolom wajib diisi.")
