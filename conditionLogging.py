import streamlit as st
import pandas as pd
import db


def page():
    conn = db.create_connection(r'/Users/tomfenemore/PycharmProjects/SailDB/local_sql.db')
    df = pd.read_sql_query('SELECT * FROM Training WHERE Debrief=0', conn)
    priority = list(df['FPriority'].unique())
    priority.append('Add')
    session = list(df['Venue']+' '+df['Date'])
    st.header('To Debrief')
    if len(session)==0:
        st.write('No sessions to debrief')
    else:
        dicc = dict(zip(session, list(df['id'])))
        wind_dir = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        wind_str = ['0-7knts', '7-12knts', '12-15knts', '15-18knts', '18-23knts', '23-27knts', '27+knts']

        ses = st.selectbox('Session', session)
        id = dicc[ses]

        str = st.select_slider('Wind Strength', options=wind_str)
        dir = st.selectbox('Wind Direction', wind_dir)
        pri = st.selectbox('Priority', priority)
        if pri == 'Add':
            pri = st.text_input('New Priority')
        notes = st.text_area('Add notes')
        video = st.file_uploader('Upload videos from this session')
        try:
            video = video.name
        except:
            video = ''

        if st.button('Add To Training Session'):
            data = (dir, str, pri, notes, video, 1, id)
            db.update_training(conn, data)

