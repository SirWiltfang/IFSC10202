
n=input("Enter Maximum Height: ")
N=int(n)
for N in range( 1 , N + 1 ):        #includes top
    print(("*" + " ") * N)

for N in range( N - 1 , 0, -1):
    print(("*" + " ") * N)

print("Thats a pointy pyramid!")