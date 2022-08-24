import streamlit as st
import conditionLogging
import db
import conditionReview
import mentalPriming
import trainingCalendar
import trainingLog

db_name = r'/Users/tomfenemore/PycharmProjects/SailDB/local_sql.db'
conn = db.create_connection(db_name)
db.create_table(conn)
conn = db.create_connection(db_name)

st.title('Dais Condition Analysis')

a = st.sidebar.selectbox('Mode', ['Mental Priming', 'To Debrief', 'Training Log', 'Condition Review',  'Training Calendar'])

if a == 'Condition Review':
    conditionReview.page()

if a == 'To Debrief':
    conditionLogging.page()

if a == 'Training Calendar':
    trainingCalendar.page()

if a == 'Training Log':
    trainingLog.page()

if a == 'Mental Priming':
    mentalPriming.page()



