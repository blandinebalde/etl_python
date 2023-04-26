# import modules
import mysql.connector
import pandas as pd

conn = mysql.connector.connect(read_default_file='C:/Users/USER/.my.cnf')
print('connexion successful')


query = "select year, title , genre , avg_vote from `oscarval_sql_course`.`imdb_movies` limit 10"
df = pd.read_sql(query, conn)

print(df.dtypes)
print("---------------------------------------")
print(df.head())

conn.close()




