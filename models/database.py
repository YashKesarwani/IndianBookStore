import re
from flask import Flask
import sqlite3

class Db:
    def __init__(self):
        try:
            self.my_conn= sqlite3.connect('BookStore.db')

        except Exception as e:
            return e
    
    def get_Connection(self):
        return self.my_conn

class Orders:
    def __init__(self):
        self.createTable()

    def createTable(self):
        try:
            obj=Db()
            db_conn=obj.get_Connection()
            curr=db_conn.cursor()
            query = """Create table if NOT EXISTS 
                CustomerMaster(userID Integer PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL ); """
            curr.execute(query)
            db_conn.commit()

            query2="""Create table if NOT EXISTS
                OrderMaster(orderID Integer AUTOINCREMENT, bookID Integer, FOREIGN KEY(bookID) REFERENCES books(ID),
                PRIMARY KEY(orderID,bookID), customerID Integer, FOREIGN KEY(customerID) REFERENCES customer (ID),
                delivery_status TEXT CHECK (delivery_status in ('packing','shipped','delivered','in-transit','failed') ));"""
            # query2="""Create table 
            #     OrderMaster(orderID Integer PRIMARY KEY AUTOINCREMENT, bookID Integer, customerID Integer, delivery_status TEXT);"""
            curr.execute(query2)
            db_conn.commit()

        except Exception as e:
            return e

    def login(self,userName,password):
        try:
            obj=Db()
            db_conn=obj.get_Connection()
            curr=db_conn.cursor()
            print("called")
            query="Insert into CustomerMaster(username,password) values('TestUser','TestPassword');"
            curr.execute(query)
            db_conn.commit()
        
        except Exception as e:
            return e
    
    def signIn(self,userID,password):
        try:
            obj=Db()
            db_conn=obj.get_Connection()
            curr=db_conn.cursor()
            query="Select * from CustomerMaster where userID=(?) and password=(?)"
            curr.execute(query,[userID,password])
            rows=curr.fetchone()
            if len(rows)>=1:
                return 1
            return 0
        except Exception as e:
            return e

    def showAll(self):
        try:
            obj=Db()
            db_conn=obj.get_Connection()
            curr=db_conn.cursor()
            query="Select * from OrderMaster;"
            curr.execute(query)
            rows=curr.fetchall()
            return rows
        
        except:
            pass
    
    def insertOrder(self,customerID,bookID):
        try:
            obj=Db()
            db_conn=obj.get_Connection()
            curr=db_conn.cursor()
            query="Insert into OrderMaster(bookID,customerID,delivery_status) values(?,?,'Packing');"
            curr.execute(query,[bookID,customerID])
            print("fucntion called")
            db_conn.commit()
        
        except Exception as e:
            return e

    def orderTracking(self,orderID):
        try:
            obj=Db()
            db_conn=obj.get_Connection()
            curr=db_conn.cursor()
            query="Select delivery_status from OrderMaster where orderID=(?)"
            curr.execute(query,[orderID])
            rows=curr.fetchone()
            if len(rows)>=1:
                return rows[0]
            return 0
        except Exception as e:
            return e