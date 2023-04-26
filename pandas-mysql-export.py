#export sql to csv

# import modules
import mysql.connector
import pandas as pd
import os

conn = mysql.connector.connect(read_default_file='C:/Users/USER/.my.cnf')
print('connexion successful')

cur_path = os.getcwd()
file = 'movies.csv'
file_path = os.path.join(cur_path, 'files', file)
print(file_path)

query = "select year, title , genre , avg_vote from `oscarval_sql_course`.`imdb_movies` where year between 2005 and 2006"
df = pd.read_sql(query, conn)

yr_2005 = df['year'] == 2005
#the file will be written with an index column
#df.to_csv(file_path)

#the file will not be written with an index column
#df.to_csv(file_path, index=0)

#the file will not be written with an index column and with the filter year = 2005
df[yr_2005].to_csv(file_path, index=0)

conn.close()




