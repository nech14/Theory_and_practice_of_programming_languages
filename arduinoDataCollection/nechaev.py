import zmq
import logging
import sqlite3
from datetime import datetime, timezone, timedelta
from tzlocal import get_localzone
import os
import time


def connect_db(name_db):
    error = None
    if not os.path.exists(name_db):
        error = "Didn't find the database and create"
    
    conn = sqlite3.connect(name_db)
        
    cursor = conn.cursor()
        
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS datas(
            id INTEGER PRIMARY KEY,
            type_data TEXT,
            data INT,
            event_time TEXT,
            event_timezone TEXT
        )
    ''')

    tz_local = get_localzone()
    current_time_local = datetime.now(tz_local)
    
    if not error is None:        
        event_data = (error, -1, current_time_local.isoformat(), tz_local.tzname(current_time_local))
        cursor.execute("INSERT INTO datas (type_data, data, event_time, event_timezone) VALUES (?, ?, ?, ?)", event_data)
    else:
        event_data = ("Reconnect", -1, current_time_local.isoformat(), tz_local.tzname(current_time_local))
        cursor.execute("INSERT INTO datas (type_data, data, event_time, event_timezone) VALUES (?, ?, ?, ?)", event_data)

    conn.commit()
    return conn, cursor





name_db = 'nechaev.db'
    
conn, cursor = connect_db(name_db)

tz_local = get_localzone()
current_time_local = datetime.now(tz_local)
event_data = ("Start programm", -1, current_time_local.isoformat(), tz_local.tzname(current_time_local))
cursor.execute("INSERT INTO datas (type_data, data, event_time, event_timezone) VALUES (?, ?, ?, ?)", event_data)
conn.commit()

context = zmq.Context()

client = context.socket(zmq.SUB)
client.connect("tcp://192.168.0.102:5555")
client.subscribe('')

count_error = 0
flag_error = True
message = ""
while True:
    tz_local = get_localzone()
    current_time_local = datetime.now(tz_local)
    try:
        message = client.recv_string(zmq.NOBLOCK)
        if len(message) < 1:
            message = "e -1"
        count_error = 0
        try:
            event_data = (message[0], message[1:], current_time_local.isoformat(), tz_local.tzname(current_time_local))
            cursor.execute("INSERT INTO datas (type_data, data, event_time, event_timezone) VALUES (?, ?, ?, ?)", event_data)
        except:
            conn, cursor = connect_db(name_db)
            event_data = (message[0], message[1:], current_time_local.isoformat(), tz_local.tzname(current_time_local))
            cursor.execute("INSERT INTO datas (type_data, data, event_time, event_timezone) VALUES (?, ?, ?, ?)", event_data)
        conn.commit()
        flag_error = True
        print(message)
    except zmq.error.Again:
        time.sleep(0.5)
        count_error += 1
        if flag_error and count_error > 10:
            count_error = 0
            flag_error = False
            message = "Error_data"
            try:
                event_data = (message, -1, current_time_local.isoformat(), tz_local.tzname(current_time_local))
                cursor.execute("INSERT INTO datas (type_data, data, event_time, event_timezone) VALUES (?, ?, ?, ?)", event_data)
            except:
                conn, cursor = connect_db(name_db)
                event_data = (message, -1, current_time_local.isoformat(), tz_local.tzname(current_time_local))
                cursor.execute("INSERT INTO datas (type_data, data, event_time, event_timezone) VALUES (?, ?, ?, ?)", event_data)
            conn.commit()

            print(message)
            
        

            
