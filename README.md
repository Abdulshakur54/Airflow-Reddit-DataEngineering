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
- The **Event Bridge Rule** can be found in [event bridge rule](./AmazonEventBridge/s3EventToStepFunction.json)

### AWS Glue
- A Glue job was create to carry out further transformation on the raw data and upload to **Redshift**
- The Glue job using Glue **Data Catalog** for both source and destination
- **Glue Crawlers** were created to update the **Data Catalogs**
- **Glue Connection** was created to the **Redshift Cluster**
- All **Glue Job, Crawlers and Connections** are in the same **VPC** as the **Redshift Cluster**
- The **Glue Scripts** can be found here [glue-job.py](./glue-job-python-script/glue-job.py)

### Redshift
- A Redshift cluster was created along with the necessary tables
- **VPC Gateway Endpoint** was created to allow **Redshift** communicate with **S3** using the **AWS Private Network**
- A *Security Group** with inbound rule allowing communication with **Glue** was used
- The **Redshift** table schema is found here [schema.json](./Redshift/schema.json)

### AWS Step Functions
- Step Functions was used to Orchestrate the workflow
- It firstly runs the **Crawler** task to crawl objects in **S3** to the **Data Catalog**
- It then runs the **Glue Job** that transforms and loads data to **Redshift**
- Finally, It runs another **Crawler** to crawl the **Redshift** data and update the **Data Catalog**
- The *Step Function** can be found here [RedditWorkflowStateMachine](./StepFunctions/RedditWorkflowStateMachine.asl.json)


******************
Thanks for Reading
******************


