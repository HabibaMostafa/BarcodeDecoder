#### This code is designed to deconstruct a barcode
#### input and parse the data so that is can be entered
#### into a mySQL database

import os

#################### Program Classes #####################

class DataEntry:
    """docstring for dataEntry"""
    def __init__(self):
        pass

    def barcode_input(self):
        self.data = input('Barcode: ')
        while(len(self.data) != 11):
            print("The barcode you entered is too short or too long - Enter a valid 11 digit barcode")
            self.data = input('Barcode: ')
        self.data = self.data.replace(" ", "")        
        list(self.data)

#######################

class BarcodeDescription:

    def __init__(self, barcode_scanned):

        self.barcode_scanned = barcode_scanned
        self.bpillar = "BP - A B-Pillar Part "
        self.front = "F  - Front Seat "
        self.back = "B  - Back Seat "
        self.driver_side = "D  - Driver Side "
        self.passenger_side ="P  - Passenger Side "
        self.defect_crater = "01 - Crater"
        self.defect_dirt = "02 - Dirt"
        self.defect_paint = "03 - Paint Run"
        self.defect_butterfly = "04 - Paint Run - Butterfly"
        self.defect_water = "05 - Water Spot"
        self.barcode_length = len(self.barcode_scanned)

#######################

    def is_bp_valid(self):

        return self.barcode_scanned[:2] == 'BP'

#######################

    def is_part_side_valid(self):

        return self.barcode_scanned[2] == 'D' or self.barcode_scanned[2] == 'P'
        
#######################

    def is_front_back_valid(self):

        return self.barcode_scanned[3] == 'F' or self.barcode_scanned[3] == 'B'

#######################

    def is_defect_type_valid(self):

        return self.barcode_scanned[4:6] == '01' or self.barcode_scanned[4:6] == '02' or self.barcode_scanned[4:6] == '03' or self.barcode_scanned[4:6] == '04' or self.barcode_scanned[4:6] == '05' 

#######################

    def is_part_type_valid(self):

        return self.barcode_scanned[6::8].isdigit()

#######################

    def is_part_num_valid(self):

        return self.barcode_scanned[8::].isdigit()

#######################

    def is_barcode_valid(self):

         return self.is_bp_valid() and self.is_part_side_valid() and self.is_front_back_valid() and self.is_defect_type_valid() and self.is_part_type_valid() and self.is_part_num_valid()

#######################

    def output_description(self):

        if (not self.is_barcode_valid()):
            print("INVALID BARCODE")
        else:
            print(self.bpillar)
            
            if (self.barcode_scanned[2] == 'P'):
                print(self.passenger_side)
            else:
                print(self.driver_side)

            if (self.barcode_scanned[3] == 'F'):
                print(self.front)
            else:
                print(self.back)
                
            if (self.barcode_scanned[4:6] == '01'):
                print(self.defect_crater)
            elif (self.barcode_scanned[4:6] == '02'):
                print(self.defect_dirt)
            elif (self.barcode_scanned[4:6] == '03'):
                print(self.defect_paint)
            elif (self.barcode_scanned[4:6] == '04'):
                print(self.defect_butterfly)
            elif (self.barcode_scanned[4:6] == '05'):
                print(self.defect_water)
            
            print("Part Type   - " + str(self.barcode_scanned[6:8]))
            print("Part Number - " + str(self.barcode_scanned[8::]))    
        
####################

class CharacterRule:

    def __init__(self, char_value, char_rule):
        self.char_value = char_value
        self.char_rule = char_rule

#################### 

    def compare_to(self, character):

        count = 0
        for rule in self.char_rule:
            if rule == character:
                count += 1

####################

class Decoder:

    def __init__(self, char_rule_array):

        self.index = 0
        self.decoderLength = len(char_rule_array)
        self.char_rule_array = char_rule_array
        self.char_rule = char_rule_array[self.index]
        
#################### Main Loop #####################

def main():
    
    alpha_list  = ['B','P','F','D']
    digit_list  = ['0','1','2','3','4','5','6','7','8','9']
    crater_list = ['1','2','3','4','5']

    test = Decoder([['B'],['P'], alpha_list, alpha_list, ['0'], crater_list, 
        digit_list, digit_list, digit_list, digit_list, digit_list])
    barcode_template = generate_magna_template(test)
    collected_data = DataEntry()
    collected_data.barcode_input()
    compare_data(barcode_template,collected_data.data)
    print("----------------Barcode Descrpition---------------\n")
    print("Barcode to be validated: " + str(collected_data.data))
    print("--------------------------------------------------")
    barcode_config = BarcodeDescription(collected_data.data)            # Passes the barcode entry (collected data) to the barcode description class.
    barcode_config.output_description()                                 # Prints out barcode entry corresponding to variables associated to them upon validation.
    print("--------------------------------------------------")

################ Program Functions #################

def generate_magna_template(OBJECT):
    c = []
    for indice in range(OBJECT.decoderLength):
            c.append(CharacterRule(indice,OBJECT.char_rule_array[indice]))

    return (c)

##########################

def compare_data(set_1, set_2):

    sum_of_ones = 0

    if(len(set_1) != len(set_2)):
        print("invalid user entry")

    for i in range(len(set_1)):
        set_1[i].compare_to(set_2[i])
        if((set_1[i].compare_to(set_2[i])) == 1):
            sum_of_ones += 1

    return sum_of_ones

##################### Program Initialization ####################

if __name__=="__main__":
    main()





