import mysql.connector


cnx = mysql.connector.connect(user='root', password='edi1998', host='localhost', database='cdscollection')

cursor = cnx.cursor()
query = 'SELECT * FROM cds'
cursor.execute(query)
cds = cursor.fetchall()

for cd in cds:
    print('CD: ' + str(cd))

cursor.close()
cnx.close()
