import sys

############################################################################################

def filesearch(file):

    while True:
        search = input("Enter search term:")

        if len(search) < 1:
            print("\nNo Search Term Entered\n")
            sys.exit()
        else:
            pass

############################################################################################

        with open(file, "r") as openfile:
        
            raw=openfile.readlines()
            line=[line.strip for line in raw]
            openfile.seek(0)
            lineindex=[]
            wordline=[]
            linecount=-1
            
            for index, line in enumerate(openfile, start = 0):
                checker = line.find(search)
                linecount+=1
                if checker == -1:
                    pass
                else:
                    a = index
                    b = line
                    lineindex.append(a)
                    wordline.append(b)
                    openfile.seek(0)
                    
#NOTE USE .INDEX_FOR_FINDING_THE_SHIT
                        
    
############################################################################################
            




############################################################################################
            
            print("line" , lineindex[0] , ":" ,wordline[0])
            print("line" , lineindex[1] , ":" ,wordline[1])
      
            
filesearch('08.Project/constitution.txt')