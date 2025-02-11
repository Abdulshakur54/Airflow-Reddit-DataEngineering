from connections.reddit_connection import connect_reddit
import pandas as pd
from etls.etls import extract_posts, transform_posts, store_in_csv
def reddit_pipeline():
    # connect to reddit
    conn = connect_reddit()
    # extract post
    posts = extract_posts(conn)
    posts_df = pd.DataFrame(posts)
    # transform post
    posts_df = transform_posts(posts_df)
    # save as csv
    return store_in_csv(posts_df)