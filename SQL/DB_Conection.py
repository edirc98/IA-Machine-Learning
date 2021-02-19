import mysql.connector

cnx = mysql.connector.connect(user='root', password='edi1998', host='localhost', database='cdscollection')



cursor = cnx.cursor()
query = 'SELECT cds.buyer FROM cds'
cursor.execute(query)
cds = cursor.fetchall()

for cd in cds:
    print('CD: ' + str(cd))

#INSERT
#insert = "INSERT INTO cds (buyer) VALUES ('%s')" % ('Amaya')
#cursor.execute(insert)
#cnx.commit()


#UPDATE
#update = "UPDATE cds SET buy_year = '2020' WHERE buyer = 'Amaya'"
#update = "UPDATE cds SET buyer = '%s' WHERE id = %i" % ('Mikel', 1)
#cursor.execute(update)
#cnx.commit()

cursor.close()
cnx.close()
