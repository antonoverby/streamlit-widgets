import streamlit as st
from st_pages import add_indentation
import sqlite3
import os

'''
Page functions:
page_layout function define things that every page should do. Instead of writing multiple lines of code at the beginning of each page, import and use the page_layout function.
'''
def page_layout():
    st.set_page_config(layout="wide")
    add_indentation()

'''
Database functions:
make_sqlite_db makes a new sqlite database and takes 3 arguments: db_file, table_name and cols. 
    # db_file is r"path/to/db_file"
    # table_name is string input
    # cols is a list of columns ***with their data types (INTEGER,TEXT, ETC)*** e.g., ["col_name1 TEXT", "col_name2 INTEGER"]
'''
def make_sqlite_db(db_file: str, table_name: str, cols: list): 
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(cols)})")
    conn.commit()
    conn.close()

def add_rows_to_db(db_file: str, table_name: str, cols: list, vals: tuple):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    query = f"INSERT INTO {table_name}({', '.join(cols)}) VALUES ({vals})"
    cursor.executemany(query)
    conn.commit()
    conn.close()
