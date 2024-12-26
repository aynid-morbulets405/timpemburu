import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import openpyxl

# Fathur
st.write("# Tugas Kelompok TIM PEMBURU (Andhika, Fathur, Frendi, dan Edi)")

# Judul Aplikasi
st.title("")

# File gambar default (pastikan file ini ada di direktori proyek)
image_path = "orang2.jpg"  # Ganti dengan nama file gambar Anda

try:
    # Membuka gambar menggunakan PIL
    image = Image.open(image_path)
    
    # Menampilkan gambar langsung
    st.image(image, caption="", use_column_width=True)

except FileNotFoundError:
    st.error(f"Tidak dapat menemukan file gambar di path: {image_path}")
    st.write("Pastikan file gambar ada di direktori yang sama dengan file kode ini.")

st.write("## Apa itu BITCOIN ????")
st.write("""
Bitcoin, mata uang kripto pionir yang muncul pada tahun 2009, telah merevolusi cara kita memandang dan menggunakan uang di era digital. 
Diciptakan oleh sosok misterius yang dikenal dengan nama samaran Satoshi Nakamoto, Bitcoin menawarkan sistem transaksi yang terdesentralisasi, 
memungkinkan pengguna untuk bertransaksi langsung tanpa perantara, dan menantang sistem keuangan tradisional yang telah ada selama berabad-abad.
""")

# Judul Aplikasi
st.title("gambaran orang diwaktu harga coin bitcoin naik")

# File gambar default (pastikan file ini ada di direktori proyek)
image_path = "hq720.jpg"  # Ganti dengan nama file gambar Anda

try:
    # Membuka gambar menggunakan PIL
    image = Image.open(image_path)
    
    # Menampilkan gambar langsung
    st.image(image, caption="hehehehe", use_column_width=True)

except FileNotFoundError:
    st.error(f"Tidak dapat menemukan file gambar di path: {image_path}")
    st.write("Pastikan file gambar ada di direktori yang sama dengan file kode ini.")

# Judul Aplikasi
st.title("Pergerakan Koin Investasi BITCOIN")

st.write("## Deskripsi Data")
st.write("Data yang digunakan adalah data Bitcoin dari 10 tahun ke belakang (2014-2024).")

# Andhika
st.write("## Visualisasi")

# Fungsi untuk membaca data dari file Excel lokal
def load_data(file_path):
    try:
        data = pd.read_excel(file_path, engine='openpyxl')
        return data
    except Exception as e:
        st.error(f"Gagal membaca file Excel: {e}")
        return None

# Fungsi untuk menampilkan visualisasi data
def visualize_data(data):
    st.title('Visualisasi Interaktif Data Bitcoin')

    # Menampilkan data
    st.write(data)

    # Plot interaktif
    st.subheader('Plot Harga Bitcoin')

    if 'Date' in data.columns and 'Close' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
        data = data.dropna(subset=['Date', 'Close'])

        # Membuat plot dengan Plotly
        fig = px.line(data, x='Date', y='Close', title='Pergerakan Harga Bitcoin', labels={'Close': 'Harga (USD)'})
        fig.update_layout(xaxis_title='Tanggal', yaxis_title='Harga (USD)')
        st.plotly_chart(fig)
    else:
        st.error("Dataset harus memiliki kolom 'Date' dan 'Close'.")

    # Menambahkan filter interaktif berdasarkan tanggal
    st.subheader('Filter Data')
    start_date = st.date_input('Mulai dari tanggal', data['Date'].min())
    end_date = st.date_input('Sampai tanggal', data['Date'].max())

    # Filter data berdasarkan tanggal
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

    # Menampilkan data yang difilter
    st.write(filtered_data)

    # Membuat plot dengan data yang difilter
    st.subheader('Plot Harga Bitcoin (Data Terfilter)')
    fig_filtered = px.line(filtered_data, x='Date', y='Close', title='Pergerakan Harga Bitcoin (Terfilter)', labels={'Close': 'Harga (USD)'})
    fig_filtered.update_layout(xaxis_title='Tanggal', yaxis_title='Harga (USD)')
    st.plotly_chart(fig_filtered)

# Fungsi utama untuk menjalankan aplikasi
def main():
    st.title("Visualisasi Data Bitcoin")

    # Jalur file Excel lokal (sesuaikan dengan nama dan lokasi file Anda)
    file_path = "databitcoin.xlsx"  # Ganti dengan path file Excel Anda

    # Memuat data dari file Excel lokal
    data = load_data(file_path)
    
    if data is not None:
        st.write(data.head())
        visualize_data(data)
    else:
        st.error("Gagal memuat data. Pastikan file Excel tersedia di direktori yang sama.")

if __name__ == '__main__':
    main()

# Frendi
st.write("## Analisis")
st.write("""
Dalam 10 tahun terakhir, harga Bitcoin mengalami fluktuasi yang signifikan. 
Pada November 2021, Bitcoin mencapai puncaknya di sekitar USD 68.789, setara dengan lebih dari Rp 1 miliar. 
Namun, harga Bitcoin juga mengalami penurunan tajam, terutama pada awal tahun 2022, di mana harga turun drastis hingga mencapai sekitar USD 30.000 pada bulan Juni 2022. 
Namun di akhir tahun 2024, Bitcoin mencapai ATH (all time high) baru di USD 107.000.
""")

st.write("Perkembangan Harga:")
st.write("""
- 2014-2016: Bitcoin mulai mendapatkan perhatian lebih luas, dengan harga yang berkisar antara USD 300 hingga USD 700.
- 2017: Tahun ini menjadi momen penting ketika Bitcoin mencapai harga hampir USD 20.000 pada bulan Desember, menarik perhatian media dan investor.
- 2018: Setelah lonjakan harga, Bitcoin mengalami penurunan yang signifikan, dengan harga terendah sekitar USD 3.200 pada bulan Desember.
- 2019-2020: Perlahan-lahan, harga mulai pulih, dan pada akhir 2020, Bitcoin kembali mencapai harga di atas USD 20.000.
- 2021: Bitcoin mencapai harga tertinggi baru di USD 64.804 pada April 2021, sebelum mengalami volatilitas yang besar.
- 2022: Setelah mencapai puncak, harga Bitcoin mengalami penurunan yang tajam, dengan beberapa bulan di mana harga berada di bawah USD 20.000.
- 2023: Memasuki tahun ini, Bitcoin menunjukkan tanda-tanda pemulihan, dengan harga kembali mendekati USD 30.000 pada pertengahan tahun.
- 2024: Memasuki akhir tahun 2024, Bitcoin mendapatkan sentimen yang positif sehingga dapat mencapai ATH sebesar USD 107.000, ini karena faktor terpilihnya presiden US Donald Trump yang pro dengan kripto.
""")

st.write("## Kesimpulan")
st.write("Kesimpulan dari perkembangan harga Bitcoin dalam dekade terakhir menunjukkan bahwa cryptocurrency ini mengalami fluktuasi yang signifikan. Dalam periode tersebut, Bitcoin mencapai puncak tertinggi di USD 68.789 pada November 2021, sebelum mengalami penurunan tajam hingga sekitar USD 30.000 pada Juni 2022. Namun, Bitcoin menunjukkan pemulihan yang kuat dan berhasil mencapai all time high (ATH) baru di USD 107.000 pada akhir tahun 2024, yang dipengaruhi oleh faktor-faktor seperti pemilihan presiden AS yang mendukung cryptocurrency. Secara keseluruhan, perjalanan harga Bitcoin mencerminkan dinamika pasar yang kompleks dan ketertarikan yang terus berkembang terhadap aset digital ini")

st.write("## Referensi / Daftar Pustaka")
st.write("https://www.tradingview.com/symbols/BTCUSD/")
st.write("https://coinmarketcap.com/currencies/bitcoin/")

# Judul Aplikasi
st.title("GAMBARAN BITCOIN MEROKET")

# Path ke file GIF lokal
gif_path = "giphy.gif"  # Ganti dengan path ke file GIF Anda

# Menampilkan GIF langsung menggunakan st.image
try:
    # Streamlit langsung menampilkan GIF yang bergerak
    st.image(gif_path, caption="$$$$$$", use_column_width=True)
except FileNotFoundError:
    st.error(f"File tidak ditemukan di path: {gif_path}")
    st.write("Pastikan file GIF tersedia di direktori proyek.")

# Judul Aplikasi
st.title("")

# Path ke file GIF lokal
gif_path = "pace2.gif"  # Ganti dengan path ke file GIF Anda

# Menampilkan GIF langsung menggunakan st.image
try:
    # Streamlit langsung menampilkan GIF yang bergerak
    st.image(gif_path, caption="", use_column_width=True)
except FileNotFoundError:
    st.error(f"File tidak ditemukan di path: {gif_path}")
    st.write("Pastikan file GIF tersedia di direktori proyek.")
