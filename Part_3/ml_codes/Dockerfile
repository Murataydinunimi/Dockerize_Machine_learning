FROM python:3.8.5
WORKDIR /project

COPY requirements.txt ./requirements.txt
COPY create_df.py ./create_df.py
COPY training_DT.py ./training_DT.py
COPY post_py.py ./post_py.py
COPY command.txt ./command.txt
COPY script.sh ./script.sh


RUN pip install -r requirements.txt

CMD ["bash","./script.sh"]


