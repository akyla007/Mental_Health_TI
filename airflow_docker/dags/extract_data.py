import os
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.sqlite.hooks.sqlite import SqliteHook
from datetime import datetime


def extract_data_to_csv(**kwargs):
    try:
        sqlite_hook = SqliteHook(sqlite_conn_id="sqlite_default")
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
        
        kwargs['ti'].xcom_push(key='dataframe', value=df.to_dict())  # Convertendo o DataFrame para dict
    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
        raise e


def save_data_to_csv(**kwargs):
    try:
        ti = kwargs['ti']
        df_dict = ti.xcom_pull(task_ids='extract_data_from_sqlite_database', key='dataframe')
        
        df = pd.DataFrame.from_dict(df_dict)
        
        df.to_csv("/opt/airflow/data/bronze/mental_health.csv", index=False)
        print(f"Dados salvos em /opt/airflow/data/bronze/mental_health.csv")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")
        raise e


with DAG(
    dag_id="extract_data_from_sqlite_database",
    start_date=datetime(2024, 12, 19),
    schedule_interval=None,  
    catchup=False,
) as dag:
    extract_data_task = PythonOperator(
        task_id="extract_data_from_sqlite_database",
        python_callable=extract_data_to_csv,
        provide_context=True,  
    )
    
    save_data_task = PythonOperator(
        task_id='save_data_to_csv',
        python_callable=save_data_to_csv,
        provide_context=True,
    )
    
    extract_data_task >> save_data_task
