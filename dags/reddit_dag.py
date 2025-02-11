from airflow.decorators import dag, task
from pendulum import datetime
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.reddit_pipeline import reddit_pipeline
from etls.etls import store_in_s3


@dag(
    schedule=None,
    start_date=datetime(2021, 1, 1, tz="Africa/Lagos"),
    catchup=False,
    default_args={"owner": "Abdulshakur", "depends_on_past": False},
)
def reddit_dag():
    @task(multiple_outputs=True)
    def reddit_task():
        return reddit_pipeline()

    @task
    def move_to_s3(filename, date):
        store_in_s3(filename, date)

    result = reddit_task()
    move_to_s3(result["filename"], result["date"])



reddit_dag()
