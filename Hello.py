import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
from streamlit.logger import get_logger

# Streamlit alkalmazás beállítása
st.title('Részvényárfolyam Megjelenítő')

# Részvényticker megadása
ticker_symbol = st.text_input('Kérlek, add meg a részvény ticker szimbólumát (pl. AAPL):')

# Dátumválasztó
start_date = st.date_input('Kezdő dátum', datetime.date(2023, 1, 1))
end_date = st.date_input('Végső dátum', datetime.date(2024, 1, 1))

# Adatok lekérése Yahoo Finance-ról
if ticker_symbol:
    try:
        # Adatok letöltése
        stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
        
        # Árfolyamadatok megjelenítése
        st.subheader(f'{ticker_symbol} Részvényárfolyama')
        st.write(stock_data)
        
        # Árfolyamok grafikonon
        st.subheader(f'{ticker_symbol} Részvényárfolyama Grafikonon')
        st.line_chart(stock_data['Close'])
        
    except Exception as e:
        st.write('Hiba történt:', e)
