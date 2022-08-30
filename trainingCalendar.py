import streamlit as st
import db
import pandas as pd

def page():
    conn = db.create_connection(r'/Users/tomfenemore/PycharmProjects/SailDB/local_sql.db')
    df = pd.read_sql_query('SELECT * FROM Training', conn)
    st.dataframe(df)
    id_list = list(df['id'].unique())
    id_list.append('None')
    id = st.selectbox('ID number of the row you would like to delete:', id_list, index=len(id_list)-1)
    if id !='None':
        st.write('Are you sure you want to delete?')
        dlt = st.button('Delete')
        if dlt==True:
            db.del_row(conn, int(id))