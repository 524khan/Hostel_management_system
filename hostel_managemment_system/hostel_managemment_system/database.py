import oracledb
try:
   con=oracledb.connect(user="system",password="524khan",dsn="localhost:1521/orcl")
except ConnectionError as err:
   print("your connerction is failed")
else:
   print("your connection is seccefully")

cur=con.cursor()
table="""
select * from customers"""
cur.execute(table)
