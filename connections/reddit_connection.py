from praw import Reddit
from airflow.models import Variable


def connect_reddit():
    aws_reddit_client_id_secret = Variable.get("aws_reddit_client_secret")
    reddit_secret_id = Variable.get("aws_reddit_secret")
    print("Connection Done")
    return Reddit(
        client_id=aws_reddit_client_id_secret,
        client_secret=reddit_secret_id,
        user_agent='user agent',
    )
