import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

#prepare cursor object
cursorObject = dataBase.cursor()

#create a dataBase
cursorObject.execute("CREATE DATABASE petshop")
print("All Done!")