# import modules
import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(read_default_file='C:/Users/USER/.my.cnf')
    print('connexion successful')
    # close your connection (very important)
    conn.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Check Credentials')
    else:
        print('err')





