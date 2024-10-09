import streamlit as st
import pandas as pd
import numpy as np

# Judul Aplikasi
st.title("Aplikasi Visualisasi Data")

# Mengunggah File CSV
uploaded_file = st.file_uploader("Pilih file CSV", type="csv")

if uploaded_file is not None:
    # Membaca dataset
    df = pd.read_csv(uploaded_file)
    
    # Menampilkan header kolom
    st.subheader("Header Kolom:")
    st.write(df.columns.tolist())
    
    # Meminta pengguna untuk memilih kolom untuk grafik
    selected_column = st.selectbox("Pilih kolom untuk ditampilkan sebagai grafik:", df.columns.tolist())
    
    # Menampilkan grafik
    st.subheader("Grafik Kolom Terpilih")
    if df[selected_column].dtype in [np.float64, np.int64]:  # Pastikan kolom adalah numerik
        st.line_chart(df[selected_column])
        st.bar_chart(df[selected_column])
    else:
        st.warning("Kolom yang dipilih bukan tipe numerik. Silakan pilih kolom numerik.")
else:
    st.info("Silakan unggah file CSV untuk memulai.")
