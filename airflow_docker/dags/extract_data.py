import os
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.sqlite.hooks.sqlite import SqliteHook
from datetime import datetime


def extract_data_to_csv():
    sqlite_hook = SqliteHook("sqlite_default")
    
    group_data_tables = """SELECT
    a.userID,
    a.surveyID,
    a.answerText,
    q.questionText,
    q.questionID
    FROM answer a
    INNER JOIN question q ON a.questionID = q.questionID
    INNER JOIN survey s ON a.surveyID = s.surveyID
    ORDER BY a.userID;
    """
    
    df = sqlite_hook.get_pandas_df(group_data_tables)
    df.to_csv("/opt/airflow/data/bronze/mental_health.csv", index=False)
    print(f"Dados extraídos e salvos em data/bronze")

with DAG(
    dag_id="extract_data_from_sqlite_database",
    start_date=datetime(2014, 12, 19),
    schedule_interval=None, # Cron tab unix
    catchup=False,
) as dag:
    extract_data_task = PythonOperator(
        task_id = "extract_data_from_sqlite_database",
        python_callable=extract_data_to_csv,
    )