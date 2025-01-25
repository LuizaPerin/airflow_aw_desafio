from airflow import DAG
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from airflow.utils.dates import datetime
from airflow.models import Variable

# set the path of your dbt project and the path to the venv activate binary as airflow variables
PATH_TO_DBT_PROJECT = Variable.get("PATH_TO_DBT_PROJECT")
PATH_TO_DBT_VENV = Variable.get("PATH_TO_DBT_VENV")

with DAG(
    dag_id='dbt_run_test_job',
    description='An Airflow DAG to invoke dbt run and dbt test',
    start_date=datetime(2025, 1, 24),
    schedule_interval="0 9 * * *",
    catchup=False,
) as dag:
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="source $PATH_TO_DBT_VENV && dbt run",
        env={"PATH_TO_DBT_VENV": PATH_TO_DBT_VENV},
        cwd=PATH_TO_DBT_PROJECT,
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="source $PATH_TO_DBT_VENV && dbt test",
        env={"PATH_TO_DBT_VENV": PATH_TO_DBT_VENV},
        cwd=PATH_TO_DBT_PROJECT,
    )

    dbt_run >> dbt_test
