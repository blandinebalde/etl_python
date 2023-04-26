# import modules
import mysql.connector

conn = mysql.connector.connect(read_default_file='C:/Users/USER/.my.cnf')
print('connexion successful')
cursor = conn.cursor()

query = "select year, title , genre from `oscarval_sql_course`.`imdb_movies` limit 10"

cursor.execute(query)

for(year, title, genre) in cursor:
    print(year, title , genre)
conn.close()




