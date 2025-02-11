import os

BATCH_SIZE = 10
OUTPUT_PATH = f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/outputs"
TIMEZONE = "Africa/Lagos"
SUBREDDIT = "news"
TARGET_NO_OF_COMMENT = 50
S3_BUCKET = 'reddit-dataengineering-92198'
POST_FIELDS = [
    "title",
    "comment_limit",
    "author_fullname",
    "clicked",
    "num_comments",
    "view_count",
    "approved_at_utc",
    "score"
]
