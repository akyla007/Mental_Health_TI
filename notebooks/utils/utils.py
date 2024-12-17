import sqlite3
import pandas as pd
import os
import sys
module_path = os.path.abspath(os.path.join(os.pardir))
if module_path not in sys.path:
    sys.path.append(module_path)

def create_connection() -> sqlite3.Connection:
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data'))
    db_file = os.path.join(base_dir, 'mental_health.sqlite')
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def query_consult(query: str) -> pd.DataFrame:
    conn = create_connection()
    
    try:
        cursor = conn.cursor()  
        cursor.execute(query)   
        rows = cursor.fetchall()  
        columns = [description[0] for description in cursor.description]  
        return pd.DataFrame(rows, columns=columns)  
    except sqlite3.Error as e:
        print(f"Erro ao executar a query: {e}")
        return pd.DataFrame()
    finally:
        conn.close()  

def read_sql_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()