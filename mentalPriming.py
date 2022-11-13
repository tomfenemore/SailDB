import pandas as pd
import db
import streamlit as st

def page():
    conn = db.create_connection(r'local_sql.db')
    df = pd.read_sql_query('SELECT * FROM Training', conn)
    venue = list(df['Venue'].unique())
    priority = list(df['FPriority'].unique())
    dayType = list(df['DayType'].unique())
    wind_dir = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    wind_str = ['0-7knts', '7-12knts', '12-15knts', '15-18knts', '18-23knts', '23-27knts', '27+knts']
    st.header('Mental Priming')
    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input('Date')
        dir = st.selectbox('Forecast Wind Direction', wind_dir)

    with col2:
        venue.append('Add')
        ven = st.selectbox('Venue', venue)
        if ven == 'Add':
            ven = st.text_input('New Venue')

    str = st.select_slider('Forecast Wind Strength', options=wind_str)

    priority.append('Add')
    pri = st.selectbox('Anticipated Priority', priority)
    if pri == 'Add':
        pri = st.text_input('New Priority')

    dayType.append('Add')
    dtyp = st.selectbox('Day Type', dayType)
    if dtyp == 'Add':
        dtyp = st.text_input('New Day Type')

    win = st.text_input('What does a winner look like?')

    data = (str, dir, date, ven, pri, dtyp, win, 0)
    if st.button('Add Training Session'):
        db.putrow(data, conn)

