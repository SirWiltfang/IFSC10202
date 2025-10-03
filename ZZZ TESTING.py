
def Convert(inputfile, outputfile):

    with open(inputfile, "r") as infile, open(outputfile, "w") as outfile:
        OUTLINES = 0
        
        while OUTLINES <=7 :
            line=str(infile.readline())

            
            outfile.write(line)

            for line in infile:
                OUTLINES += 1
        
        print(f"Conversion complete. Total lines written: {OUTLINES}")


Convert("07.Project/07.Project Angles Input.txt", "07.Project/07.Project Angles Output.txt" )