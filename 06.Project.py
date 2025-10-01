
input_path = '06.Project Input File.txt'
merger_path = '06.Project Merge File.txt'
output_path = '06.Project Output File.txt'

def combine_files(input_path , merger_path , output_path):
    
    with open(input_path , "r") as input1:
        content_1 = input1.read()
    
    with open(merger_path , "r") as merger1:
        content_2 = merger1.read()
    
    with open(output_path , "r") as combined_files:
        combined_files.write(content_1)
        combined_files.write(content_2)


#remove bullshit section----------------------------------

mid = len(content_1) // 2

#merge files section------------------------------------------

input_a = content_1[:mid]
input_b = content_1[mid:]

print(input_a)