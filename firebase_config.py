import streamlit as st
import firebase_admin
from firebase_admin import credentials, db

@st.cache_resource
def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(st.secrets["firebase_credentials"])
        firebase_admin.initialize_app(cred, {
            "databaseURL": "https://cloud-computing-1ce46-default-rtdb.asia-southeast1.firebasedatabase.app"
        })
    return db
