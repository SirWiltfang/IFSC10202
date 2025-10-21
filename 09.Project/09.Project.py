
import csv
import sys

#############

def Distances(file):
    data = []
    maxwidth = 0
    
###############################

    with open(file, 'r') as openfile:

        for line in openfile:
            line = line.strip()
            
            if not line:
                continue

            y = line.split(',')

            cleanrow = []
            for item in y:
                cleanitem = item.strip()
                cleanrow.append(cleanitem)

                if len(cleanitem) > maxwidth:
                    maxwidth = len(cleanitem)

            data.append(cleanrow)

        align = maxwidth +2

##############################

        for row in data:
            for item in row:
                print(f"{item:>{align}}" , end = '')
            print()

###############################
    
        fromsearch = input("Enter From City: ")
        tosearch = input("Enter To City: ")

        fromcitys = data[0][:]
        tocitys = data[:][0]

        if fromsearch in data[0][:]:
            firstcoord = (fromcitys.index(fromsearch))
        else:
            print("\nInvalid From City\n")
            sys.exit()
        
        if tosearch in data[:][0]:
            secondcoord = (tocitys.index(tosearch))
        else:
            print("\nInvalid To City\n")
            sys.exit()
        
        print(f"{fromsearch} to {tosearch} - {data[firstcoord][secondcoord]} miles")
        

Distances('09.Project/09.Project Distances.csv')