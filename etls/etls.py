from constants.constants import (
    BATCH_SIZE,
    SUBREDDIT,
    POST_FIELDS,
    OUTPUT_PATH,
    TIMEZONE,
    TARGET_NO_OF_COMMENT,S3_BUCKET
)
from praw import Reddit
import pandas as pd
import numpy as np
import pendulum
import logging
import boto3
from botocore.exceptions import ClientError


def extract_posts(conn: Reddit) -> list[dict]:
    posts = conn.subreddit(SUBREDDIT).top(time_filter='day',limit=BATCH_SIZE)
    extracted_posts = []
    print('How are you')
    for post in posts:
        post = vars(post)
        sub_post = {key: post[key] for key in POST_FIELDS}
        extracted_posts.append(sub_post)
    return extracted_posts


def transform_posts(posts: pd.DataFrame) -> pd.DataFrame:
    posts["meet_comment_criteria"] = np.where((posts["num_comments"] >= TARGET_NO_OF_COMMENT), True, False)
    posts['approved_at_utc'] = pd.to_datetime(posts['approved_at_utc'], unit='s')
    return posts

def store_in_csv(posts: pd.DataFrame):
    ts = pendulum.now(TIMEZONE)
    date = pendulum.DateTime(ts.year,ts.month,ts.day,ts.hour,ts.minute,ts.second).format("YYYYMMDDHHmm")
    filename = f"file_{date}.csv"
    posts.to_csv(f"{OUTPUT_PATH}/{filename}",index=False)
    return {"filename":filename, "date":date}


def store_in_s3(filename: str, date: str):
    print(f"filename is {filename}")
    key = f"raw/date={date}/{filename}"
    s3_client = boto3.client('s3')
    filepath = f"{OUTPUT_PATH}/{filename}"
    print(filepath)
    try:
        s3_client.upload_file(filepath, S3_BUCKET, key)
    except ClientError as e:
        logging.error(e)




