import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    create_table_sql = r'CREATE TABLE IF NOT EXISTS Training (id integer PRIMARY KEY, ' \
                  r'WindStrength text, ' \
                  r'WindDirection text,' \
                  r'FWindStrength text, ' \
                  r'FWindDirection text,' \
                  r'FPriority text,' \
                  r'DayType text,'\
                  r'Winner text,'\
                  r'Priority text,' \
                  r'Date text,' \
                  r'Venue text,' \
                  r'Notes text,' \
                  r'Video text,' \
                  r'Debrief integer);'
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def putrow(data, conn):
    sql = f'INSERT INTO Training (FWindStrength,FWindDirection,Date,Venue,FPriority,DayType,Winner,Debrief) VALUES (?,?,?,?,?,?,?,?)'
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()

def select_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Training")
    rows = cur.fetchall()
    return(rows)

def update_training(conn, training):
    sql = ''' UPDATE Training
                  SET 
                      WindDirection = ?,
                      WindStrength = ? ,
                      Priority = ?,
                      Notes = ?,
                      Video = ?,
                      Debrief = ?
                  WHERE 
                      id = ?'''
    cur = conn.cursor()
    cur.execute(sql, training)
    conn.commit()

def del_row(conn, id):
    sql = 'DELETE FROM Training WHERE id = ?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()