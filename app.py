import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Aplikasi Analisis Data Sederhana")

uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.write(df.head())

    st.write("### Statistik Deskriptif")
    st.write(df.describe())

    column = st.selectbox("Pilih kolom numerik untuk visualisasi", df.select_dtypes(include="number").columns)

    st.write("### Histogram")
    fig, ax = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax)
    st.pyplot(fig)

    st.write("### Boxplot")
    fig2, ax2 = plt.subplots()
    sns.boxplot(x=df[column], ax=ax2)
    st.pyplot(fig2)
