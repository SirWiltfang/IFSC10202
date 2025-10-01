def merge(input , merger , output):

    input_o = open(input_path, 'r')
    merger_o = open(merger_path, 'r')
    outputw = open(output_path, 'w')

##########################

    input_c = input_o.read()
    merger_c = merger_o.read()
    
    x = input_c.find('**')
    y = input_c.rfind('**')+2
    f = input_c.replace(input_c[x:y] , merger_c)

##############################

    outputw.write(f)
    outputw.close()
    
    input_o.seek(0)
    merger_o.seek(0)


    a = len(input_o.readlines()) -1
    b = len(merger_o.readlines())
    c = len(outputw.readlines())
    print(a)
    print(b)
    print(c)

    input_o.close()
    merger_o.close()
    outputr.close()

##################################

merge("06.Project Input File.txt" , "06.Project Merge File.txt" ,  "06.Project Output File.txt")
