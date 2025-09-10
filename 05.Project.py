
s=int(input("Enter Start of Range:"))

e=int(input("Enter End of Range:"))

for n in range(s,e):
    z = int(n%10)
    x = int((n/10)%10)
    c = int((n/100)%10)
    v = int((n/1000)%10)
    
    if (n/10) < 1:
        print(n)
    else:
        if (n/100) < 1:
            if n==(z**2)+(x**2):
                print(n)
        else:
            if (n/1000) < 1:
                if n==(z**3)+(x**3)+(c**3):
                    print(n)
            else:
                 if (n/10000) < 1:
                      if n==(z**4)+(x**4)+(c**4)+(v**4):
                          print(n)
    
    
