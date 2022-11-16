FROM jupyter/scipy-notebook

WORKDIR /project


COPY create_df.py ./create_df.py
COPY training_DT.py ./training_DT.py

RUN python3 create_df.py 

