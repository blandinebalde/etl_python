#export sql to csv

# import modules
import mysql.connector
import pandas as pd
import os

conn = mysql.connector.connect(read_default_file='C:/Users/USER/.my.cnf')
print('connexion successful')

cur_path = os.getcwd()
file = 'movies_rating.csv'
file_path = os.path.join(cur_path, 'files', file)
print(file_path)

query = "select year, title , genre , avg_vote , case when avg_vote < 3 then  'bad' when avg_vote < 6 then  'okay' when avg_vote >=6 then 'good' end as movie_rating from `oscarval_sql_course`.`imdb_movies` where year between 2005 and 2006"
df = pd.read_sql(query, conn)

yr_2005 = df['year'] == 2005
df.to_csv(file_path, index= False)


conn.close()




