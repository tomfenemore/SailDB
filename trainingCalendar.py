import streamlit as st
import db
import pandas as pd

def page():
    st.write('calender here')
    conn = db.create_connection(r'/Users/tomfenemore/PycharmProjects/SailDB/local_sql.db')
    df = pd.read_sql_query('SELECT * FROM Training', conn)
    st.dataframe(df)