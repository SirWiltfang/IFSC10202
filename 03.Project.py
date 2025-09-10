

x=int(input("Enter First number:"))
y=input("Enter Operator (+,-,/,*):")
z=int(input("Enter Second number:"))

valid_operators = ["+" , "-" , "/", "*"]

if y not in valid_operators :
    print("Invalid Operator")
else:
    num1 = x
    num2 = z
    if y == "+" :
        w = x + z
        print(w)
    else:
        if y == "-" :
            w = x - z
            print(w)
        else:
            if y == "/" :
                w = x / z
                print(w)
            else:
                if y == "*" :
                    w = x * z
                    print(w)


