import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

all_df = pd.read_csv("all_data.csv")

all_df['dateday'] = pd.to_datetime(all_df['dateday'])

st.title("Dashboard Analisis Penyewaan Sepeda 🚲")

st.header("Perbandingan Penyewaan Sepeda Berdasarkan Cuaca dan Hari Libur")
weather_counts = all_df.groupby(["weathersit_hour", "holiday_hour"])['cnt_hour'].mean().reset_index()

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
st.write("\n\n💡 **Insight:** Cuaca cerah adalah kondisi terbaik untuk penyewaan sepeda, karena memiliki jumlah penyewaan tertinggi.Hari kerja memiliki tingkat penyewaan lebih tinggi dibandingkan hari libur, kemungkinan karena penggunaan sepeda untuk keperluan kerja atau sekolah.Cuaca buruk (hujan ringan & hujan lebat) menyebabkan penurunan drastis dalam penyewaan sepeda, yang berarti pengguna cenderung menghindari bersepeda saat hujan.")

st.header("Pola Penyewaan Sepeda Sepanjang Hari")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=all_df['hour'], y=all_df['cnt_hour'], estimator='mean', ci=None, ax=ax)
ax.set_title("Pola Penyewaan Sepeda Sepanjang Hari")
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.set_xticks(range(0, 24))
st.pyplot(fig)

st.write("\n\n💡 **Insight:** Jam sibuk penyewaan sepeda terjadi pada pukul 08:00 dan 17:00, sesuai dengan jam berangkat dan pulang kerja/sekolah.Penyewaan sepeda sangat rendah pada dini hari (00:00 - 05:00), menunjukkan bahwa penggunaan sepeda pada waktu ini sangat terbatas. Siang hari memiliki penyewaan yang cukup stabil, tetapi tidak setinggi jam sibuk. Malam hari penyewaan mulai menurun, kemungkinan karena berkurangnya aktivitas luar ruangan.")


with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.write("**Nama:** Dimas Nurcahya")
    st.write("**Email:** dimasnurcahya478@gmail.com")
    st.write("**ID Dicoding:** [dimas_nch]")

    
    
