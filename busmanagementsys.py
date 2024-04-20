#bus management system

print("***BUS BOOKING SYSTEM***")

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="shreya#2016")

mycursor=mydb.cursor()

mycursor.execute("create database if not exists bus")

mycursor.execute("use bus")

#creating required tables

mycursor.execute("create table if not exists bus_info(busno char(4) primary key,departuretime float(5),arrivaltime float(5),source char(10),destination char(10))")

mydb.commit()

mycursor.execute("create table if not exists passengerinfo(busno char (4),seatno int(3),pname varchar(30),dot date,foreign key(busno) references bus_info(busno))")

mydb.commit()

def install():

    busno=input("enter bus no")

    departuretime=float(input("enter dtime"))

    arrivaltime=float(input("enter atime"))

    source=input("enter station from")

    destination=input("enter station to")

    mycursor.execute("insert into bus_info values('"+busno+"','"+str(departuretime)+"','"+str(arrivaltime)+"','"+source+"','"+destination+"')")

    mydb.commit()

    print("bus record added")

def reservation():

    busno=input("enter bus no")

    seatno=int(input("enter seat no less than 32"))

    passengername=input("enter passenger name")

    dot=str(input("enter date of travel in yyyy-mm-dd format"))

    mycursor.execute("insert into passengerinfo values('"+busno+"','"+str(seatno)+"','"+passengername+"','"+dot+"')")

    mydb.commit()

    print("passenger information added")

def busavailable():

    mycursor.execute("select * from bus_info")

    for i in mycursor:

        print(i)

def showreservation():

    mycursor.execute("select * from bus_info,passengerinfo where bus_info.busno = passengerinfo.busno")

    for i in mycursor:

        print(i)

def cancelreservation():

    busno=input("enter bus no")

    mycursor.execute("delete from passengerinfo where busno = '"+busno+"'")

    mydb.commit()

    print("record deleted")

while True:

    print("1. install")

    print("2. reservation")

    print("3. busavailable")

    print("4. showreservation")

    print("5. cancelreservation")

    print("6. exit")

    ch=int(input("enter choice"))

    if ch==1:

        install()

    elif ch==2:

        reservation()

    elif ch==3:

        busavailable()

    elif ch==4:

        showreservation()

    elif ch==5:

        cancelreservation()

    else:

        print("Exit")

        break
