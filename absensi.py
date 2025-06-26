from datetime import datetime
from firebase_config import init_firebase

def simpan_absensi(nama):
    db = init_firebase()
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ref = db.reference("absensi")
    ref.push({
        "nama": nama,
        "waktu": waktu,
        "status": "Hadir"
    })
    return waktu
