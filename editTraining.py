import streamlit as st
import db
import pandas as pd


def page():
    conn = db.create_connection(r'/Users/tomfenemore/PycharmProjects/SailDB/local_sql.db')
    df = pd.read_sql_query('SELECT * FROM Training', conn)
    st.dataframe(df)
    id_list = list(df['id'].unique())
    id_list.append('None')
    id = st.selectbox('ID number of the row you would like to edit:', id_list, index=len(id_list)-1)
    if id !='None':
        data_row = df[df['id']==id]

        st.subheader('Mental Priming')
        venue = list(df['Venue'].unique())
        priority = list(df['FPriority'].unique())
        dayType = list(df['DayType'].unique())
        wind_dir = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        wind_str = ['0-7knts', '7-12knts', '12-15knts', '15-18knts', '18-23knts', '23-27knts', '27+knts']
        st.header('Mental Priming')

        win = st.text_input('What does a winner look like?', value=data_row['Winner'].iloc[0])
        notes = st.text_area('Add notes', value=data_row['Notes'].iloc[0])
        video = st.file_uploader('Upload videos from this session')
        try:
            video = video.name
        except:
            video = ''
        data = (win, notes, video, id)
        if st.button('Finish Edit'):
            db.edit_notes(data, conn)