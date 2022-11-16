#!/usr/bin/env python
# coding: utf-8

from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import os
import create_df as cd
import training_DT as tT
import psycopg2
import pandas as pd
from sqlalchemy import create_engine




class DatabaseManager:

    def __init__(self):
        #self.db_url = 'postgresql://{user}:{password}\\@{hostname}/postgres'
        #self.db_url = self.db_url.format(
            #user=os.environ['DB_USER'],
            #password=os.environ['DB_PASSWORD'],
            #hostname=os.environ['DB_HOST'])

        db_name = 'postgres'
        db_user = os.environ["DB_USER"]
        db_pass = os.environ["DB_PASSWORD"]
        db_host = os.environ["DB_HOST"]
        db_port = os.environ["DB_PORT"]

        self.db_url='postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)

        print("Connection_String:",self.db_url)
        self.db = create_engine(self.db_url)
        self.conn = self.db.connect()
        #self.conn = self.db.raw_connection()
        self.conn_psy = psycopg2.connect(self.db_url)
        self.conn_psy.autocommit = True
        self.cursor = self.conn_psy.cursor()
                        

        print("Connection to Postgre is successful")


    def add_data(self, data):
        data.to_sql("iris_df", con=self.conn, if_exists= 'replace', index = False)
        print("Data is added successfully")
        


    def command(self):

        command_path = os.path.join(os.getcwd(),"./command.txt")
        with open(command_path,'r') as f:
            query_list = f.readlines()
            query = query_list[0]
        
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        
        print("Command is executed successfully")
        print("The table is filtered with the following query:",query)
        return res

        

    def verify(self):


        sql2 = ''' SELECT column_name, data_type, is_nullable
        FROM information_schema.columns
        WHERE table_name = 'iris_df';   '''

        self.cursor.execute(sql2)
        for i in self.cursor.fetchall():
            print(i)

        print("The table is being printed")

        

    def commit(self):
        self.conn_psy.commit()

        print("Changes are commited successfully")
        
                                            

    def close(self):
        self.conn_psy.close()

        print("Connection is closed successfully")


if __name__ == '__main__':


    try:

        iris_df, path= cd.create_load_iris()

        sql_session = DatabaseManager()
        sql_session.add_data(iris_df)
        sql_session.commit()
        sql_session.verify()
        result_df = sql_session.command()
        sql_session.close()




        df = pd.DataFrame(result_df, columns=['sepal_length', 'sepal_width', 'petal_length','petal_width','target'])
        df.to_csv("sql_df.csv", index=False)
        print("Postgre output is ready at:", os.getcwd())
        print("The df has the following shape:",np.shape(df))

    except Exception as e:
        print(e)


