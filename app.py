import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import altair as alt

st.title("pergerakan koin investasi BITCOIN")


#fathur
st.write("# Tugas Kelompok Tim Pemburu")

st.write("## Pendahuluan")
st.write("Bitcoin, mata uang kripto pionir yang muncul pada tahun 2009, telah merevolusi cara kita memandang dan menggunakan uang di era digital. Diciptakan oleh sosok misterius yang dikenal dengan nama samaran Satoshi Nakamoto, Bitcoin menawarkan sistem transaksi yang terdesentralisasi, memungkinkan pengguna untuk bertransaksi langsung tanpa perantara, dan menantang sistem keuangan tradisional yang telah ada selama berabad-abad.")

st.write("## Deskripsi Data")
st.write("data yang digunakan adalah data bitcoin dari 10 tahun ke belakang")

#andhika
st.write("## Visualisasi")
# Load the data
def load_data():
    file_path = 'databitcoin.xlsx'  # Replace with your local file path if testing locally
    data = pd.ExcelFile(file_path)
    df = data.parse('Sheet1')
    df_cleaned = df.iloc[:, 0].str.split(';', expand=True)
    df_cleaned.columns = [
        "timeOpen", "timeClose", "timeHigh", "timeLow", "name", 
        "open", "high", "low", "close", "volume", "marketCap", "timestamp"
    ]
    # Ensure all columns are strings before processing
    df_cleaned = df_cleaned.applymap(lambda x: x if isinstance(x, str) else str(x))
    # Convert relevant columns to numeric and time formats
    df_cleaned["timeOpen"] = pd.to_datetime(df_cleaned["timeOpen"].str.replace('"', '', regex=False), errors='coerce')
    df_cleaned["open"] = pd.to_numeric(df_cleaned["open"], errors='coerce')
    df_cleaned["high"] = pd.to_numeric(df_cleaned["high"], errors='coerce')
    df_cleaned["low"] = pd.to_numeric(df_cleaned["low"], errors='coerce')
    df_cleaned["close"] = pd.to_numeric(df_cleaned["close"], errors='coerce')
    return df_cleaned

data = load_data()

# Streamlit App
st.title("Interactive Bitcoin Visualization")

st.sidebar.header("Filter Options")

# Date range filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    [data["timeOpen"].min(), data["timeOpen"].max()],
    min_value=data["timeOpen"].min(),
    max_value=data["timeOpen"].max()
)

# Filter data based on date range
filtered_data = data[(data["timeOpen"] >= pd.Timestamp(date_range[0])) & (data["timeOpen"] <= pd.Timestamp(date_range[1]))]

# Display filtered data
st.write("### Filtered Data", filtered_data)

# Plotting
chart = alt.Chart(filtered_data).mark_line().encode(
    x='timeOpen:T',
    y=alt.Y('close:Q', title='Closing Price'),
    tooltip=['timeOpen:T', 'close:Q']
).properties(
    title="Bitcoin Closing Prices Over Time",
    width=800,
    height=400
)

st.altair_chart(chart, use_container_width=True)

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
