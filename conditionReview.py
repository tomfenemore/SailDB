import streamlit as st
import datetime
import pandas as pd
import db
import plotly.express as px



def page():
    conn = db.create_connection(r'/Users/tomfenemore/PycharmProjects/SailDB/local_sql.db')
    df = pd.read_sql_query('SELECT * FROM Training', conn)
    venue = list(df['Venue'].unique())
    ven = st.sidebar.selectbox('Venue', venue)
    for i in venue:
        if ven == i:
            if ven != 'All':
                df = df[df['Venue'] == ven]
            st.header(ven)
            diag = st.sidebar.selectbox('Diagram', ['Wind Strength', 'Wind Direction'])
            if diag == 'Wind Strength':
                fig = px.line_polar(df, theta=df['WindStrength'].value_counts().index,
                                    r=df['WindStrength'].value_counts(), line_close=True, category_orders={
                        'r': ['0-7knts', '7-12knts', '12-15knts', '15-18knts', '18-23knts']})  #
                st.plotly_chart(fig, use_container_width=True)

            if diag == 'WindDirection':
                fig = px.line_polar(df, theta=df['WindDirection'].value_counts().index,
                                    r=df['WindDirection'].value_counts(), line_close=True,
                                    category_orders={'r': ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']})  #
                st.plotly_chart(fig, use_container_width=True)

