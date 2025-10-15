import sys

def filesearch(file):
    while True:
        search = input("Enter search term:")

        if len(search) < 1:
            print("\nNo Search Term Entered\n")
            sys.exit()
        else:
            pass
            FILE_LINES = []
############################################################################################
    
        with open(file, "r") as openfile:
            
            file_content = openfile.read()
            openfile.seek(0)
            
            raw=openfile.readlines()
            line=[line.strip for line in raw]
            openfile.seek(0)
            
            lineindex=[]
            wordline=[]
            linecount=-1
            linecountshit = []
            file_lines = []
            
            openfile.seek(0)
            
            start_offset = 0

        with open(file, "r") as openfile_lines:
             raw_lines_with_newlines = openfile_lines.readlines()


        with open(file, "r") as openfile:
             file_content = openfile.read()

             linecountshit = []
             
             for index, line in enumerate(raw_lines_with_newlines, start = 0):

                 processed_line = line.strip()
                 h = processed_line
                 file_lines.append(h)

                 checker = line.find(search)
                 linecount+=1
                 if checker == -1:
                     pass
                 else:
                     c = linecount
                     a = index
                     b = line

                     linecountshit.append(c)
                     lineindex.append(a)
                     wordline.append(b)
            
             if linecountshit:
                 
                 start_line_index = linecountshit[0]
                 start_offset = 0
                 
                 for i in range(start_line_index):
                     start_offset += len(raw_lines_with_newlines[i])
                     
                 print(file_content.find("\n\n", start_offset))
             else:
                 print("Search term not found.")
                       

        

###################################################



            #print(linecountstart[1])
            #print("line" , lineindex[1] , ":" ,wordline[0])
            #print("split\n")
            #print("line" , lineindex[1] , ":" ,wordline[1])

filesearch('08.Project/constitution.txt')