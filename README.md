## Reddit Data Engineering 

#### This project extracted posts (blog) data from Reddit API using **Airflow**.  
#### It ingested it into **S3** which triggers an **Event Bridge Rule** that targets a **Step Function**.  
#### The **Step Function** Orchestrate the workflow by running a **Glue Crawler** task to crawl the **S3 Objects**,  
#### followed by a **Glue Job** that performs further transformation, followed by loading the data into ***Redshift**.  
#### The step function concludes by running a **Glue Crawler Job** that crawls the Redshift Table 



### Airflow
- Airflow was deployed in a **docker** environment
- A secret backend using **AWS Secret Manager** was configured to handle secrets.
- **Postgres** was used as the meta data store
- **PGBouncer** was used to handle connection pooling of the **Postgres Database** 

### S3
- Two S3 buckets were created. One to store the ingested reddit files, the other to serve as a staging environment for **Glue** and **Redshift Cluster**
- The S3 bucket that stored the ingested files was configured to send notifications to **Amazon Event Bridge**
- The S3 was created in same region as **Glue** and **Redshift** to avoid cost and foster low latency data transfer

### Amazon Event Bridge
- An **Event Bridge Rule** was configured to target a **Step Function** once an object is uploaded in the **S3 bucket**
- The **Event Bridge Rule** can be seen ![image](./StepFunctions/statefunction%20image.png)

