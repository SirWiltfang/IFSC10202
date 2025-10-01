def merge(input_path, merger_path, output_path):

    input_o = open(input_path, 'r')
    merger_o = open(merger_path, 'r')
    outputw = open(output_path, 'w')

    a = -1
    for line in input_o:
        a += 1
    input_o.seek(0) 

    b = 0
    for line in merger_o:
        b += 1
    merger_o.seek(0)
    
    A= str(a)
    B= str(b)
    print( A + " input file records")
    print( B + " merge file records")

    ##########################
    
    for line in input_o:
        if "**Insert Merge File Here**" in line:
            for m_line in merger_o:
                outputw.write(m_line)
        else:
            outputw.write(line)

    ##############################

    outputw.close()
    
    outputr = open(output_path, 'r')
    c = len(outputr.readlines())
    C= str(c)
    print( C + " output file records")

    input_o.close()
    merger_o.close()
    outputr.close() 
    
##################################

merge("06.Project Input File.txt", "06.Project Merge File.txt", "06.Project Output File.txt")