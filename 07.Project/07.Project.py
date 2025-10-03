
def Convert(inputfile, outputfile):

    OUTLINES = 0
    with open(inputfile, "r") as infile:
        with open(outputfile, "w") as outfile:

            for line in infile:
                OUTLINES += 1

                x = line.find(chr(176))
                Deg= int((line[:x]))

                y = line.find("'")
                Min= int(line[x+1:y])
                dem1 = Min/60

                z = line.find('"')
                Sec= int(line[y+1:z])
                dem2 = Sec/3600
                
                FinalDeg = Deg + dem1 + dem2
                Final = str(FinalDeg)

                outfile.write(Final+"\n")

    print(f"\n{OUTLINES} records processed\n")
        


Convert("07.Project/07.Project Angles Input.txt", "07.Project/07.Project Angles Output.txt" )