import streamlit as st
import conditionLogging
import db
import conditionReview
import editTraining
import mentalPriming
import trainingCalendar
import trainingLog

db_name = r'local_sql.db'
conn = db.create_connection(db_name)
db.create_table(conn)
conn = db.create_connection(db_name)

st.title('Dais Condition Analysis')

a = st.sidebar.selectbox('Mode', ['Mental Priming', 'To Debrief', 'Training Log',   'Training Calendar', 'Edit Training']) #'Condition Review',

#if a == 'Condition Review':
    #conditionReview.page()

if a == 'To Debrief':
    conditionLogging.page()

if a == 'Training Calendar':
    trainingCalendar.page()

if a == 'Training Log':
    trainingLog.page()

if a == 'Mental Priming':
    mentalPriming.page()

if a == 'Edit Training':
    editTraining.page()



