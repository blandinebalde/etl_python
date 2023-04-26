#export sql to csv

# import modules
import mysql.connector
import pandas as pd
import os

conn = mysql.connector.connect(read_default_file='C:/Users/USER/.my.cnf')
print('connexion successful')

cur_path = os.getcwd()
file = 'city_housing.csv'
file_path = os.path.join(cur_path, 'files', file)
print(file_path)

query = "select * from oscarval_sql_course.city_house_prices"


df = pd.read_sql(query, conn)

#data transformation steps
df.set_index('Date', inplace=True)
df = df.stack().reset_index()
df.columns = ['date' , 'city' , 'price']

df.to_csv(file_path, index=False)

conn.close()




