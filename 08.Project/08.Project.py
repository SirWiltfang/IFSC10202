
import sys

################################################

def filesearch(file):

    with open(file, "r") as openfile:
        FILE_LINES = [line.rstrip('\n') for line in openfile.readlines()]

    linecount = len(FILE_LINES)

    while True:
        search = input("Enter search term:")

        if len(search) < 1:
            print("\nNo Search Term Entered\n")

        else:
            pass

################################################################

            last_printed = -1

            for index, line in enumerate(FILE_LINES):
                
                if search in line:

                    if index > last_printed:

                        start_index = index

                        while start_index > 0 and FILE_LINES[start_index -1] != "":
                            start_index-=1
                        
                        if start_index > 0 and FILE_LINES[start_index -1] == "":
                            start_index -= 1 

#################################

                        end_index = index

                        while end_index < linecount and FILE_LINES[end_index] != "":
                            end_index+=1
                        if end_index < linecount:
                            end_index+=1 

#############################################
                        
                        for section_num in range(start_index , end_index):
                            line_content = FILE_LINES[section_num]
                            print("line" , section_num , ":" , line_content)

                        print(" ")

                        last_printed = end_index -1

                    else:
                        pass

filesearch('08.Project/constitution.txt')