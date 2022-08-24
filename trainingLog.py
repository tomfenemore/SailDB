import streamlit as st
from streamlit_card import card
import pandas as pd
import db


def page():
    conn = db.create_connection(r'/Users/tomfenemore/PycharmProjects/SailDB/local_sql.db')
    df = pd.read_sql_query('SELECT * FROM Training WHERE Debrief=1', conn)
    st.header('Condition Logging')
    venue = list(df['Venue'].unique())
    venue.append('All')
    ven = st.sidebar.selectbox('Venue', venue)
    fore = st.sidebar.selectbox('Forecast or True', ['Forecast', 'True'])
    if fore == 'Forecast':
        d = 'FWindDirection'
        s = 'FWindStrength'
    if fore == 'True':
        d = 'WindDirection'
        s = 'WindStrength'
    st.header(ven)
    col1, col2, col3 = st.columns(3)
    for i in venue:
        if ven == i:
            if ven != 'All':
                df = df[df['Venue'] == ven]

    direction = list(df[d].unique())
    direction.append('All')
    dir = st.sidebar.selectbox('Direction', direction)
    for i in direction:
        if dir == i:
            if dir != 'All':
                df = df[df[d] == dir]

    strength = list(df[s].unique())
    strength.append('All')
    stren = st.sidebar.selectbox('Strength', strength)
    for i in strength:
        if stren == i:
            if stren != 'All':
                df = df[df[s] == stren]



    for i in range(len(df)):
        if i % 3 == 0:
            with col1:
                with st.expander(df['Date'].iloc[i] + ' ' + df['Venue'].iloc[i]):
                    st.write('Wind: ' + df['WindStrength'].iloc[i] + ' ' + df['WindDirection'].iloc[i])
                    st.write('Forecast: ' + df['FWindStrength'].iloc[i] + ' ' + df['FWindDirection'].iloc[i])
                    st.write('Priority:' +df['Priority'].iloc[i])
                    st.write('Expected Priority:' + df['FPriority'].iloc[i])
                    st.write('Notes: ' + df['Notes'].iloc[i])
                    st.write('Video: ' + df['Video'].iloc[i])

        elif i % 3 == 1:
            with col2:
                with st.expander(df['Date'].iloc[i] + ' ' + df['Venue'].iloc[i]):
                    st.write('Wind: ' + df['WindStrength'].iloc[i] + ' ' + df['WindDirection'].iloc[i])
                    st.write('Forecast: ' + df['FWindStrength'].iloc[i] + ' ' + df['FWindDirection'].iloc[i])
                    st.write('Priority:' + df['Priority'].iloc[i])
                    st.write('Expected Priority:' + df['FPriority'].iloc[i])
                    st.write('Notes: ' + df['Notes'].iloc[i])
                    st.write('Video: ' + df['Video'].iloc[i])
        elif i % 3 == 2:
            with col3:
                with st.expander(df['Date'].iloc[i] + ' ' + df['Venue'].iloc[i]):
                    st.write('Wind: ' + df['WindStrength'].iloc[i] + ' ' + df['WindDirection'].iloc[i])
                    st.write('Forecast: ' + df['FWindStrength'].iloc[i] + ' ' + df['FWindDirection'].iloc[i])
                    st.write('Priority:' + df['Priority'].iloc[i])
                    st.write('Expected Priority:' + df['FPriority'].iloc[i])
                    st.write('Notes: ' + df['Notes'].iloc[i])
                    st.write('Video: ' + df['Video'].iloc[i])

