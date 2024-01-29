FROM python:3.8

RUN pip install requests pymongo

COPY data_retrieval_script.py /data_retrieval_script.py

RUN chmod +x /data_retrieval_script.py

CMD ["python", "/data_retrieval_script.py"]
