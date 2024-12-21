import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.title("pergerakan koin investasi BITCOIN")


#fathur
st.write("# Tugas Kelompok Tim Pemburu")

st.write("## Pendahuluan")
st.write("Bitcoin, mata uang kripto pionir yang muncul pada tahun 2009, telah merevolusi cara kita memandang dan menggunakan uang di era digital. Diciptakan oleh sosok misterius yang dikenal dengan nama samaran Satoshi Nakamoto, Bitcoin menawarkan sistem transaksi yang terdesentralisasi, memungkinkan pengguna untuk bertransaksi langsung tanpa perantara, dan menantang sistem keuangan tradisional yang telah ada selama berabad-abad.")

st.write("## Deskripsi Data")
st.write("data yang digunakan adalah data bitcoin dari 10 tahun ke belakang")

#andhika
st.write("## Visualisasi")
# Membaca data dari file Excel
file_path = '/mnt/data/databitcoin.xlsx'
data = pd.read_excel(file_path)

# Menampilkan data di Streamlit
st.title('Visualisasi Interaktif Data Bitcoin')
st.write(data)

# Membuat plot interaktif
st.subheader('Plot Harga Bitcoin')
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Close'], label='Harga Penutupan')
plt.xlabel('Tanggal')
plt.ylabel('Harga (USD)')
plt.title('Pergerakan Harga Bitcoin')
plt.legend()
st.pyplot(plt)

# Menambahkan widget interaktif
st.subheader('Filter Data')
start_date = st.date_input('Mulai dari tanggal', data['Date'].min())
end_date = st.date_input('Sampai tanggal', data['Date'].max())

# Filter data berdasarkan tanggal
filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

# Menampilkan data yang difilter
st.write(filtered_data)

# Membuat plot dengan data yang difilter
st.subheader('Plot Harga Bitcoin (Data Terfilter)')
plt.figure(figsize=(10, 5))
plt.plot(filtered_data['Date'], filtered_data['Close'], label='Harga Penutupan')
plt.xlabel('Tanggal')
plt.ylabel('Harga (USD)')
plt.title('Pergerakan Harga Bitcoin (Terfilter)')
plt.legend()
st.pyplot(plt)

# Menjalankan aplikasi Streamlit
if __name__ == '__main__':
    st.run()
st.write("Gunakan juga elemen-elemen interaktif `streamlit`.")

st.write("## Analisis")
st.write("Dalam 10 tahun terakhir, harga Bitcoin mengalami fluktuasi yang signifikan. Pada November 2021, Bitcoin mencapai puncaknya di sekitar USD 68.789, setara dengan lebih dari Rp 1 miliar. Namun, harga Bitcoin juga mengalami penurunan tajam, terutama pada awal tahun 2022, di mana harga turun drastis hingga mencapai sekitar USD 30.000 pada bulan Juni 2022. tetapi diakhir tahun 2024 bitcoin mencapai ATH all time high nya lagi mencapai USD 107.000")
("Perkembangan Harga:")
("2014-2016: Bitcoin mulai mendapatkan perhatian lebih luas, dengan harga yang berkisar antara USD 300 hingga USD 700.")
("2017: Tahun ini menjadi momen penting ketika Bitcoin mencapai harga hampir USD 20.000 pada bulan Desember, menarik perhatian media dan investor.")
("2018: Setelah lonjakan harga, Bitcoin mengalami penurunan yang signifikan, dengan harga terendah sekitar USD 3.200 pada bulan Desember.")
("2019-2020: Perlahan-lahan, harga mulai pulih, dan pada akhir 2020, Bitcoin kembali mencapai harga di atas USD 20.000.")
("2021: Bitcoin mencapai harga tertinggi baru di USD 64.804 pada April 2021, sebelum mengalami volatilitas yang besar.")
("2022: Setelah mencapai puncak, harga Bitcoin mengalami penurunan yang tajam, dengan beberapa bulan di mana harga berada di bawah USD 20.000.")
("2023: Memasuki tahun ini, Bitcoin menunjukkan tanda-tanda pemulihan, dengan harga kembali mendekati USD 30.000 pada pertengahan tahun.")
("2024: Memasuki akhir tahun di 2024 bitcoin mendapatkan sentimen yang positif sehingga dapat mencapai ATH nya sebesar USD 107.000 ini karena faktor terpilih nya presiden US Donald Trump yang pro dengan kripto")

#frendi
st.write("## Kesimpulan")
st.write("Tuliskan butir-butir kesimpulan dari analisis.")

st.write("## Referensi / Daftar Pustaka")
st.write("https://www.tradingview.com/symbols/BTCUSD/.")
