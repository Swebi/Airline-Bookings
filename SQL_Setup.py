import mysql.connector as sqlcon

mycon = sqlcon.connect(host="localhost", user="root", password="suhayb")

if mycon.is_connected():
    print("Connected")
    cursor1 = mycon.cursor()
    cursor1.execute("create database if not exists flight;")
    cursor1.execute("use flight;")
    cursor1.execute("CREATE TABLE IF NOT EXISTS userpass (username varchar(12) NOT NULL,password varchar(12) NOT NULL,PRIMARY KEY (username)) ;")
    cursor1.execute("CREATE TABLE IF NOT EXISTS bookhist (customerid varchar(6) NOT NULL,departuredate date DEFAULT NULL,departure varchar(45) DEFAULT NULL,arrival varchar(45) DEFAULT NULL,airline varchar(45) DEFAULT NULL,distance int DEFAULT NULL,fare int DEFAULT NULL,seat varchar(45) DEFAULT NULL,meal varchar(45) DEFAULT NULL,price int DEFAULT NULL) ;")
    cursor1.execute("insert into userpass values('user','user');")

    mycon.commit()
    mycon.close()


