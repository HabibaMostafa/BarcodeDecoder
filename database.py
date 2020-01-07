from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
import decoder

#################### Program Classes #####################
class Database():

    def __init__(self):
        self.DB_NAME = 'Barcode'

#####################

    def connect(self):
        self.cnx = mysql.connector.connect(  host="localhost",
                                user="git",
                                passwd="123",
                                database="mydb"  )
        self.cursor = self.cnx.cursor()

#####################

    def create_database(self):

        try:
            self.cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

#####################

    def create_table(self):

        self.table = "BARCODE"

        self.cursor.execute("CREATE TABLE IF NOT EXISTS BARCODE (Barcode VARCHAR(50), BPillarPart VARCHAR(50), PassengerDriverSide VARCHAR(50), FrontBackSeat VARCHAR(50), DefectType VARCHAR(50), PartType VARCHAR(50), PartNum VARCHAR(50), Filepath VARCHAR(50))")

        print("Table Created")

#####################

    def end_connection(self):

        self.cursor.close()
        self.cnx.close()

#####################

    def insert_record(self, array):

        # new_array = [('1', array[0], array[1], array[2], array[3], array[4], array[5], array[6])]

        path = "/Desktop/" + array[0]

        print(array)

        # query = """INSERT INTO MAGNA1 (Barcode, BPillarPart, PassengerDriverSide, FrontBackSeat, DefectType, PartType, PartNum) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""

        self.cursor.execute("""INSERT INTO BARCODE (Barcode, BPillarPart, PassengerDriverSide, FrontBackSeat, DefectType, PartType, PartNum, Filepath) 
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""", (array[0], array[1], array[2], array[3], array[4], array[5], array[6], path))
        self.cnx.commit()

        print("Inserted")
