from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
import database
import decoder

#################### Main Loop #####################

def main():

    alpha_list  = ['B','P','F','D']
    digit_list  = ['0','1','2','3','4','5','6','7','8','9']
    crater_list = ['1','2','3','4','5']

    connect = database.Database()
    connect.connect()
    # connect.create_database()
    connect.create_table()
    test = decoder.Decoder([['B'],['P'], alpha_list, alpha_list, ['0'], crater_list, 
        digit_list, digit_list, digit_list, digit_list, digit_list])
    barcode_template = decoder.generate_template(test)
    while True:
        collected_data = decoder.DataEntry()
        collected_data.barcode_input()
        decoder.compare_data(barcode_template,collected_data.data)
        print("----------------Barcode Descrpition---------------\n")
        print("Barcode to be validated: " + str(collected_data.data))
        print("--------------------------------------------------")
        barcode_config = decoder.BarcodeDescription(collected_data.data)           
        barcode_config.output_description()                                 
        print("--------------------------------------------------")
        array = barcode_config.export_barcode()
        connect.insert_record(array)
    connect.end_connection()


##################### Program Initialization ####################

if __name__=="__main__":
    main()



