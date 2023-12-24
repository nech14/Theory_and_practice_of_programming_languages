
import sqlite3
from datetime import datetime, timezone, timedelta
from tzlocal import get_localzone
import os

name_db = 'nechaev.db'

def connect_db(name_db):
    error = None
    if not os.path.exists(name_db):
        error = "Didn't find the database"
    
    conn = sqlite3.connect(name_db)
        
    cursor = conn.cursor()
        
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS datas(
            id INTEGER PRIMARY KEY,
            type_data TEXT,
            data REAL,
            event_time TEXT,
            event_timezone TEXT
        )
    ''')

    if not error is None:
        event_data = (error, -1, current_time_local.isoformat(), tz_local.tzname(current_time_local))
        cursor.execute("INSERT INTO datas (type_data, data, event_time, event_timezone) VALUES (?, ?, ?, ?)", event_data)


    return conn, cursor



tz_local = get_localzone()

current_time_local = datetime.now(tz_local)

type_data = 'ERROR'
data = -1

conn, cursor = connect_db(name_db)

event_data = (type_data, data, current_time_local.isoformat(), tz_local.tzname(current_time_local))


cursor.execute("INSERT INTO datas (type_data, data, event_time, event_timezone) VALUES (?, ?, ?, ?)", event_data)

conn.commit()

conn.close()
