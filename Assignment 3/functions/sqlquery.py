import os
import sqlite3
import pandas as pd

data_url = 'students.csv'
headers = ['id','first_name','last_name','amount_due']
data_table = pd.read_csv(data_url, header=None, names=headers)

# Clear example.db if it exists
if os.path.exists('student.db'):
    os.remove('student.db')

# Create a database
conn = sqlite3.connect('student.db', check_same_thread=False)

# Add the data to our database
data_table.to_sql('data_table', conn, dtype={
    'id':'INT',
    'first_name':'VARCHAR(256)',
    'last_name':'VARCHAR(256)',
    'amount_due':'INT',
})

conn.row_factory = sqlite3.Row

# Make a convenience function for running SQL queries
def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows
