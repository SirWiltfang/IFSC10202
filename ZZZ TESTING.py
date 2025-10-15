import sys

#################

def filesearch(file):

    while True:
        search = input("Enter search term:")

        if len(search) < 1:
            print("\nNo Search Term Entered\n")
            sys.exit()
        else:
            pass

        with open(file, "r") as openfile:
        
            raw=openfile.readlines()
            line=[line.strip for line in raw]
            openfile.seek(0)
            lineindex=[]
            wordline=[]
            linecount=-1
            startline = []
            for index, line in enumerate(openfile, start = 0):
                checker = line.find(search)
                linecount+=1
                linecountstart = []
                if checker == -1:
                    pass
                else:
                   a = line
                   b = index
                   lineindex.append(b)
                   wordline.append(a)
                   checker = 0
                   for line in (openfile):
                       while checker ==-1:
                           linecount-=1
                           line.rfind("\n\n", index)
                           a = line
                           b = linecount
                           startline.append(a)
                           linecountstart.append(b)


                   
                       

        

###################################################



            print(linecountstart[1])
            print("line" , lineindex[1] , ":" ,wordline[0])
            print("split\n")
            print("line" , lineindex[1] , ":" ,wordline[1])

filesearch('08.Project/constitution.txt')