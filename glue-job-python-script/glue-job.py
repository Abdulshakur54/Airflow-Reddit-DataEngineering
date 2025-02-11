import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1739173155790 = glueContext.create_dynamic_frame.from_catalog(
    database="reddit-database-crawler",
    table_name="raw",
    transformation_ctx="AWSGlueDataCatalog_node1739173155790",
)

# Script generated for node Change Schema
ChangeSchema_node1739173217320 = ApplyMapping.apply(
    frame=AWSGlueDataCatalog_node1739173155790,
    mappings=[
        ("title", "string", "title", "string"),
        ("comment_limit", "long", "comment_limit", "int"),
        ("author_fullname", "string", "author_fullname", "string"),
        ("clicked", "boolean", "clicked", "boolean"),
        ("num_comments", "long", "num_comments", "int"),
        ("view_count", "string", "view_count", "string"),
        ("approved_at_utc", "string", "approved_at_utc", "string"),
        ("score", "long", "score", "int"),
        ("meet_comment_criteria", "boolean", "meet_comment_criteria", "boolean"),
        ("date", "string", "date", "string"),
    ],
    transformation_ctx="ChangeSchema_node1739173217320",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1739173435751 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node1739173217320,
    database="reddit-database-crawler",
    table_name="reddit_database_reddit_schema_reddit_table",
    redshift_tmp_dir="s3://redshift-glue-temp-storage-32897",
    transformation_ctx="AWSGlueDataCatalog_node1739173435751",
)

job.commit()
