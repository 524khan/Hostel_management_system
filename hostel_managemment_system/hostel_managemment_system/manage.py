import oracledb
try:
   con=oracledb.connect(user="system",password="524khan",dsn="localhost:1521/orcl")
except ConnectionError as err:
   print("your connection is fallied")
else:
   print("i love zahra")
cur=con
