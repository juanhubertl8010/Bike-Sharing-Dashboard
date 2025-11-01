import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

st.title("🚴‍♂️ Bike Sharing Dashboard")


df = pd.read_csv("hour.csv")

if "dteday" in df.columns:
    df["dteday"] = pd.to_datetime(df["dteday"])

weather_mapping = {
    1: "Clear",
    2: "Mist",
    3: "Light Rain",
    4: "Heavy Rain"
}

if "weathersit" in df.columns:
    df["weather_desc"] = df["weathersit"].map(weather_mapping)

st.sidebar.header("🗓️ Filter Tanggal")
if "dteday" in df.columns:
    min_date = df["dteday"].min()
    max_date = df["dteday"].max()
    start_date, end_date = st.sidebar.date_input(
        "Pilih rentang tanggal:",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )
    df = df[(df["dteday"] >= pd.to_datetime(start_date)) & (df["dteday"] <= pd.to_datetime(end_date))]

col1, col2, col3 = st.columns(3)
with col1:
    total_users = df["cnt"].sum()
    st.metric("👥 Total Jumlah Pengguna", f"{total_users:,}")

with col2:
    if "temp" in df.columns:
        avg_temp = df["temp"].mean() * 41
        st.metric("🌡️ Suhu Udara Rata-Rata", f"{avg_temp:.2f} °C")
    else:
        st.metric("🌡️ Suhu Udara Rata-Rata", "N/A")

with col3:
    if "weathersit" in df.columns:
        most_common_weather = df["weather_desc"].mode()[0]
        st.metric("☁️ Cuaca Dominan", most_common_weather)
    else:
        st.metric("☁️ Cuaca Dominan", "N/A")

st.divider()

if "hr" in df.columns and "cnt" in df.columns:
    st.subheader("🕒 Jumlah Pengguna Berdasarkan Jam")
    hourly_data = df.groupby("hr")["cnt"].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=hourly_data, x="hr", y="cnt", marker="o", ax=ax)
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Pengguna")
    st.pyplot(fig)
