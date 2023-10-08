import tabula
import pandas as pd, numpy as np

import streamlit as st
import re
import string

uploaded_file = st.file_uploader("Choose a file", accept_multiple_files=False, type = ['pdf'])

if uploaded_file is not None:
#     uploaded_file = uploaded_file.read()

    dfs = tabula.read_pdf(uploaded_file, pages='all')
    df = dfs[1].loc[6:]
    df = df.dropna(subset = ['Mobile'])
    df['Transaction Date'] = df['Mobile'].str.split().str[:2].str.join(' ')
    df['Post Date']= df['Mobile'].str.split().str[2:].str.join(' ')

    df = df[['Transaction Date', 'Post Date', 'Phone', 'Unnamed: 1']]
    df.columns = ['Transaction Date', 'Post Date', 'Description', 'Amount']

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
   )
