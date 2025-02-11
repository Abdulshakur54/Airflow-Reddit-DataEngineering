FROM apache/airflow:2.10.4-python3.12

USER root
RUN apt-get -y update
WORKDIR /home/airflow
COPY requirements.txt ./

USER airflow
RUN pip install --no-cache-dir -r ./requirements.txt
