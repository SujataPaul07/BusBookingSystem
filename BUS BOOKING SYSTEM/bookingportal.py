import mysql.connector
from datetime import date
import random

import string
"""--------Asansol To Kolkata Bus Booking Code------------"""
def bus1(connection,cur):
     pName = input("Enter Passenger Name : ")
     pAge  = int(input("Enter Passenger Age : "))
     pCon = int(input("Enter Contact Number : "))
     date_components = input('Enter The Boarding Date (YYYY-MM-DD) :').split('-')
     year, month, day = [int(item) for item in date_components]
     boarding_date = date(year, month, day)
     depart = "Asansol"
     arrival = "Kolkata"
     ticket_number = ''.join(random.choices(string.ascii_uppercase+string.digits, k=7))
     query = "insert into bus1(passenger_name, passenger_age,contact,boarding_date,departed,arrival,ticket_number) values(%s,%s,%s,%s,%s,%s,%s)"
     values = (pName,pAge,pCon,boarding_date,depart,arrival,ticket_number)
     cur.execute(query,values)
     connection.commit()
     print("Bus Booked Successfully.")
     
     print("-------------------------------------------------")
     print("Booking Details")
     print("-------------------------------------------------")
     print("Passenger Name : ",pName)
     print("Passenger Age : ",pAge)
     print("Contact : ",pCon)
     print("Boarding Date : ",boarding_date)
     print("Departing Place : ",depart)
     print("Arriving Place : ",arrival)
     print("Ticket Number : ",ticket_number)
     print("-------------------------------------------------")
     
"""--------Asansol To Dhanbad  Bus Booking Code------------"""
def bus2(connection,cur):
     pName = input("Enter Passenger Name : ")
     pAge  = int(input("Enter Passenger Age : "))
     pCon = int(input("Enter Contact Number : "))
     date_components = input('Enter The Boarding Date (YYYY-MM-DD) :').split('-')
     year, month, day = [int(item) for item in date_components]
     boarding_date = date(year, month, day)
     depart = "Asansol"
     arrival = "Dhanbad"
     ticket_number = ''.join(random.choices(string.ascii_uppercase+string.digits, k=7))
     query = "insert into bus2(passenger_name, passenger_age,contact,boarding_date,departed,arrival,ticket_number) values(%s,%s,%s,%s,%s,%s,%s)"
     values = (pName,pAge,pCon,boarding_date,depart,arrival,ticket_number)
     cur.execute(query,values)
     connection.commit()
     print("Bus Booked Successfully.")
     
     print("-------------------------------------------------")
     print("Booking Details")
     print("-------------------------------------------------")
     print("Passenger Name : ",pName)
     print("Passenger Age : ",pAge)
     print("Contact : ",pCon)
     print("Boarding Date : ",boarding_date)
     print("Departing Place : ",depart)
     print("Arriving Place : ",arrival)
     print("Ticket Number : ",ticket_number)
     print("-------------------------------------------------")
     
"""-------------Asansol To Kolkata Update Portal Code---------------"""   
def Bus1Update(connection,cur):
    ticket_number = input("Enter Your Ticket Number :")
    query = "select exists(select 1 from bus1 where ticket_number = %s)"
    
    cur.execute(query,(ticket_number,))
    result = cur.fetchone();
    if(result[0]==1):
        print("Ticket Number Exists In Our Database")
        pName = input("Enter Updated Passenger Name : ")
        pAge  = int(input("Enter Updated Passenger Age : "))
        pCon = int(input("Enter Updated Contact Number : "))
        date_components = input('Enter The Updated Boarding Date (YYYY-MM-DD) :').split('-')
        year, month, day = [int(item) for item in date_components]
        boarding_date = date(year, month, day)
        depart = "Asansol"
        arrival = "Kolkata"
        updateQuery = "update bus1 set passenger_name = %s , passenger_age = %s, contact=%s, boarding_date = %s,departed = %s, arrival = %s where ticket_number = %s"
        values = (pName,pAge,pCon,boarding_date,depart,arrival,ticket_number)

        cur.execute(updateQuery,values);
        connection.commit();
        print("Data Updated Successfully.")
        
        print("-------------------------------------------------")
        print("Updated Booking Details")
        print("-------------------------------------------------")
        print("Passenger Name : ",pName)
        print("Passenger Age : ",pAge)
        print("Contact : ",pCon)
        print("Boarding Date : ",boarding_date)
        print("Departing Place : ",depart)
        print("Arriving Place : ",arrival)
        print("Ticket Number : ",ticket_number)
        print("-------------------------------------------------\n\n")
    else:
        print("Ticket Number Does Not Exists In Our Database" ) 
            
           
"""-------------Asansol To Dhanbad Update Portal Code---------------""" 
def Bus2Update(connection,cur):
    ticket_number = input("Enter Your Ticket Number :")
    query = "select exists(select 1 from bus2 where ticket_number = %s)"
    
    cur.execute(query,(ticket_number,))
    result = cur.fetchone();
    if(result[0]==1):
        print("Ticket Number Exists In Our Database")
        pName = input("Enter Updated Passenger Name : ")
        pAge  = int(input("Enter Updated Passenger Age : "))
        pCon = int(input("Enter Updated Contact Number : "))
        date_components = input('Enter The Updated Boarding Date (YYYY-MM-DD) :').split('-')
        year, month, day = [int(item) for item in date_components]
        boarding_date = date(year, month, day)
        depart = "Asansol"
        arrival = "Kolkata"
        updateQuery = "update bus2 set passenger_name = %s , passenger_age = %s, contact=%s, boarding_date = %s,departed = %s, arrival = %s where ticket_number = %s"
        values = (pName,pAge,pCon,boarding_date,depart,arrival,ticket_number)

        cur.execute(updateQuery,values);
        connection.commit();
        print("Data Updated Successfully.")
        
        print("-------------------------------------------------")
        print("Updated Booking Details")
        print("-------------------------------------------------")
        print("Passenger Name : ",pName)
        print("Passenger Age : ",pAge)
        print("Contact : ",pCon)
        print("Boarding Date : ",boarding_date)
        print("Departing Place : ",depart)
        print("Arriving Place : ",arrival)
        print("Ticket Number : ",ticket_number)
        print("-------------------------------------------------\n\n")
    else:
        print("Ticket Number Does Not Exists In Our Database") 
            

"""-------------Asansol To Kolkata Delete Portal Code---------------"""    
def Bus1Delete(connection,cur):
    ticket_number = input("Enter Your Ticket Number :")
    query = "select exists(select 1 from bus1 where ticket_number = %s)"
    
    cur.execute(query,(ticket_number,))
    result = cur.fetchone();
    if(result[0]==1):
        deleteQuery = "delete from bus1 where ticket_number = %s"
        cur.execute(deleteQuery,(ticket_number,))
        connection.commit()
        print("Deleted Successfully.")
    else:
        print("Ticket Number Not Found In The Database")
        
"""-------------Asansol To Dhanbad Delete Portal Code---------------"""     
def Bus2Delete(connection,cur):
    ticket_number = input("Enter Your Ticket Number :")
    query = "select exists(select 1 from bus2 where ticket_number = %s)"
    
    cur.execute(query,(ticket_number,))
    result = cur.fetchone();
    if(result[0]==1):
        deleteQuery = "delete from bus2 where ticket_number = %s"
        cur.execute(deleteQuery,(ticket_number,))
        connection.commit()
        print("Deleted Successfully.")
    else:
        print("Ticket Number Not Found In The Database")
    
# Python Mysql Connection Code
def main():
    connection = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='bus_booking'
        
    )
    cur = connection.cursor()
    if(cur):
        print("Database Connection Established Successfully.")
    else:
        print("Database Not Connected.")
    choice=0
    while(choice<=6):
        print("--------PYTHON TRAVEL AGENCY----------")
        print("1. Asansol To Kolkata Bus Booking")
        print("2. Asansol To Dhanbad Bus Booking")
        print("--------UPDATE PORTAL----------- -------")
        print("3. Asansol To Kolkata Update Booking Details")
        print("4. Asansol To Dhanbad Update Booking Details")
        print("--------DELETE PORTAL----------- -------")
        print("5. Delete Asansol To Kolkata Booking Details")
        print("6. Delete Asansol To Dhanbad Booking Details")
        print("7. Exit")
        print("----------------------------------------")
        
        
    
        choice = int(input("Enter Your Journey Choice : "))
        if(choice==1):
            print("This is booking portal for Asansol to Kolkata")
            bus1(connection, cur)
        elif(choice ==2):
            print("This is the booking portal for Asansol To Dhanbad")
            bus2(connection, cur)
        elif(choice==3):
            print("This is the update booking portal for Asansol To Kolkata")
            Bus1Update(connection,cur)
        elif(choice==4):
            print("This is the update booking portal for Asansol To Dhanbad")
            Bus2Update(connection,cur)
        elif(choice==5):
            print("This is the update booking portal for Asansol To Dhanbad")
            Bus1Delete(connection,cur)
        elif(choice==6):
            print("This is the update booking portal for Asansol To Dhanbad")
            Bus2Delete(connection,cur)
        
        
        else:
            print("Thanks For Visiting Us")
        
#Calling Main Function
main()
    