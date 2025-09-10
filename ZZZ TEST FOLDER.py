

x=float(input("Enter first value: "))
y=(input("Enter Operator (+,-,/,*): "))
z=float(input("Enter second number: "))

valid_operators = ["+" , "-" , "/", "*"]

if y not in valid_operators:
    print("Invalid Operator")
else:
    w = x , y , z
    print(w)