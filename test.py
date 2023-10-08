import tabula
import pandas as pd, numpy as np

import streamlit as st
import re
import string

uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True, type = ['pdf'])
n_files = len(uploaded_files)

if uploaded_files is not None:

    ### Case 1: Single PDF ###
    if (len(uploaded_files) == 1):
        file = uploaded_files[0]
        file_path = file.read()
        
        # get total number of pages in PDF
#         parser = PDFParser(file)
#         document = PDFDocument(parser)
#         n_pages_file = resolve1(document.catalog['Pages'])['Count']
        
        dfs = tabula.read_pdf(file_path, pages='all')
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
