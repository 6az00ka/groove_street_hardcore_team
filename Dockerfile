FROM python:3.8.9

WORKDIR /app

COPY . .

RUN pip3 install numpy networkx matplotlib

# VOLUME [ "/app/data" ]

CMD ["python", "task_3_velikanov.py"]

# RUN docker cp task_3_plt_con:/app/data /Users/ivanvelikanov/TestData