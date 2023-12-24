
from datetime import datetime, timedelta
from matplotlib.dates import date2num, DateFormatter
import matplotlib.pyplot as plt
import numpy as np
import sqlite3

def get_data(db_name, name):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(f"SELECT data, event_time FROM datas WHERE type_data = '{name}'")
    rows = cursor.fetchall()
    conn.close()
    rows = np.array(rows)
    return rows

def print_p(rows):
    plt.figure(figsize=(18, 12))

    time_array = np.array([datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f') for dt in rows[:, 1]])

    plt.plot(time_array, rows[:, 0])

    start_date = min(time_array)
    end_date = max(time_array)

    time_array = np.arange(start_date, end_date, timedelta(hours=5)).astype(datetime)

    y_values = np.arange(0, 1024, 50)
    date_format = DateFormatter('%Y-%m-%d %H:%M:%S')
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.xticks(time_array, rotation=45, ha='right')
    plt.yticks(y_values)

    plt.savefig('my_plot.png')

def print_hist(rows, name):
    plt.figure(figsize=(18, 12))

    time_array = np.array([datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f') for dt in rows])

    plt.hist(time_array)

    start_date = min(time_array)
    end_date = max(time_array)

    time_array = np.arange(start_date, end_date, timedelta(hours=5)).astype(datetime)

    y_values = np.arange(0, 20, 1)
    date_format = DateFormatter('%Y-%m-%d %H:%M:%S')
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.xticks(time_array, rotation=45, ha='right')

    plt.savefig(f'{name}.png')


rows = get_data('nechaev.db', 'p')
print_p(rows)

rows = get_data('nechaev.db', 't')
print_hist(rows[:, 1], 't')

rows = get_data('nechaev.db', 'm')
print_hist(rows[:, 1], 'm')

print('create')

