# my-new-ripository
import csv
import psycopg2

con=psycopg2.connect("dbname='import_csv' user='csv' host='localhost' password='1234' port='5432'")

cur=con.cursor()

reader=csv.reader(open('/home/swetha/Desktop/free-zipcode-database.csv','r'))
#select load_csv_file("csvtable",'/home/swetha/Desktop/free-zipcode-database.csv',16)

for row in reader:
	cur.execute("INSERT INTO newdata VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]))
	con.commit()
	cur.execute("SELECT * FROM newdata;")

rows=cur.fetchall()

for row in rows:
	print row

	

   

   
	
       
 

