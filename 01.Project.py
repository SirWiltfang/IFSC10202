y = input("Enter the time in seconds:")
n = int(y)
Z = "Seconds"
X = "Minutes"
C = "Hours"
V = "Days"
B = "Years"
if n/60 < 1:
    u = str(n)
    W = u + " " + Z
    print(W)
else:
     S = n%60
     e = str(S)
     W = e + " " + Z
     print(W)
     #end of seconds
     floatval1 = n / 60
     m = int(floatval1)

     if m/60 < 1:
          e = str(m)
          W = e + " " + X
          print(W)
     else:
          M = m%60
          e = str(M)
          W = e + " " + X
          print(W)
          #end of minutes
          floatval2 = m / 60
          h = int(floatval2)

          if h/24 < 1:
               e = str(h)
               W= e + " " + C
               print(W)
          else:
               H = h%24
               e = str(H)
               W = e + " " + C
               print(W)
               #end of hours
               floatval3 = h/24
               d = int(floatval3)

               if d/365 < 1:
                    e = str(d)
                    W = e + " " + V
                    print(W)
               else:
                    D = d%365
                    e = str(D)
                    W = e +  " " + V
                    print(W)
                    #end of days
                    floatval4 = d/365
                    Y = int(floatval4)
                    e = str(Y)
                    W = e +  " " + B
                    print(W)
                    #end of years

#floatvala = 1.5
#b = (int(floatvala))*4
#print(b)
