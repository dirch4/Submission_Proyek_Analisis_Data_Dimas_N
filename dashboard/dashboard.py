import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
all_df = pd.read_csv("https://raw.githubusercontent.com/dirch4/Submission_Proyek_Analisis_Data_Dimas_N/refs/heads/main/dashboard/all_data.csv")
all_df['dateday'] = pd.to_datetime(all_df['dateday'])

# Sidebar
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.write("**Nama:** Dimas Nurcahya")
    st.write("**Email:** dimasnurcahya478@gmail.com")
    st.write("**ID Dicoding:** [dimas_nch]")
    
    # Filter interaktif
    start_date = st.date_input("Pilih tanggal mulai", all_df['dateday'].min())
    end_date = st.date_input("Pilih tanggal akhir", all_df['dateday'].max())
    selected_weather = st.multiselect("Pilih kondisi cuaca", all_df['weathersit_hour'].unique(), all_df['weathersit_hour'].unique())
    st.markdown("""
    **Keterangan Kondisi Cuaca:**
    - **1** = Cerah
    - **2** = Berawan
    - **3** = Hujan Ringan
    - **4** = Hujan Lebat
    """)
# Filter dataset berdasarkan input
filtered_df = all_df[(all_df['dateday'] >= pd.Timestamp(start_date)) & (all_df['dateday'] <= pd.Timestamp(end_date)) & (all_df['weathersit_hour'].isin(selected_weather))]

st.title("Dashboard Analisis Penyewaan Sepeda 🚲")

# Visualisasi 1: Perbandingan Penyewaan Sepeda Berdasarkan Cuaca dan Hari Libur
st.header("Perbandingan Penyewaan Sepeda Berdasarkan Cuaca dan Hari Libur")
weather_counts = filtered_df.groupby(["weathersit_hour", "holiday_hour"])['cnt_hour'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    x="weathersit_hour",
    y="cnt_hour",
    hue="holiday_hour",
    data=weather_counts,
    palette=["royalblue", "darkorange"],
    hue_order=[0, 1],
    ax=ax
)
ax.set_title("Perbandingan Penyewaan Sepeda Berdasarkan Cuaca dan Hari Libur", fontsize=14)
ax.set_xlabel("Kondisi Cuaca", fontsize=12)
ax.set_ylabel("Rata-rata Penyewaan Sepeda", fontsize=12)
ax.set_xticks(range(4))
ax.set_xticklabels(["Cerah", "Berawan", "Hujan Ringan", "Hujan Lebat"], fontsize=10)
ax.legend(title="Tipe Hari", labels=["Hari Kerja", "Hari Libur"], fontsize=12)
st.pyplot(fig)

st.write("\n\n💡 **Insight:** Cuaca cerah adalah kondisi terbaik untuk penyewaan sepeda, dengan jumlah penyewaan tertinggi. Penyewaan lebih tinggi pada hari kerja dibandingkan hari libur. Cuaca buruk menyebabkan penurunan drastis dalam penyewaan sepeda.")

# Visualisasi 2: Pola Penyewaan Sepeda Sepanjang Hari
st.header("Pola Penyewaan Sepeda Sepanjang Hari")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=filtered_df['hour'], y=filtered_df['cnt_hour'], estimator='mean', ci=None, ax=ax)
ax.set_title("Pola Penyewaan Sepeda Sepanjang Hari")
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.set_xticks(range(0, 24))
st.pyplot(fig)

st.write("\n\n💡 **Insight:** Jam sibuk penyewaan sepeda terjadi pada pukul 08:00 dan 17:00, sesuai dengan jam berangkat dan pulang kerja/sekolah. Penyewaan sangat rendah pada dini hari (00:00 - 05:00) dan mulai menurun di malam hari.")
