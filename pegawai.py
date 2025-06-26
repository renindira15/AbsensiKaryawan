from firebase_config import init_firebase

def simpan_pegawai(nip, nama, jabatan):
    db = init_firebase()
    ref = db.reference(f"pegawai/{nip}")
    ref.set({
        "nip": nip,
        "nama": nama,
        "jabatan": jabatan
    })
