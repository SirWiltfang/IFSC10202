import csv

def Distances(file):
    data = []
    max_width = 0

    with open(file, 'r') as openfile:
        for line in openfile:
            line = line.strip()
            if not line:
                continue
                
            y = line.split(',')
            
            cleaned_row = []
            for item in y:
                clean_item = item.strip()
                cleaned_row.append(clean_item)
                
                if len(clean_item) > max_width:
                    max_width = len(clean_item)
            
            data.append(cleaned_row)
    
    ALIGN_WIDTH = max_width + 2 
    
    for row in data:
        for item in row:
            print(f"{item:>{ALIGN_WIDTH}}", end='')
            
        print()
        


Distances('09.Project/09.Project Distances.csv')