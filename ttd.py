def largest(x, y, z):
    s=[x,y,z]
    if (check_int_float(x) and check_int_float(y) and check_int_float(z)):
        return max(s)
    elif (check_int_float(x) and check_int_float(y) and check_int_float(z)):
        return max(s)
    elif (check_int_float(x) and check_int_float(y) and check_int_float(z)):
        return max(s)
    else:
        return "error"

def check_int_float(x):
    if(type(x)== int or type(x) == float):
        return True
    else:
        return False

'''x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
z = int(input("Enter third number:"))

r = largest(x, y, z)

print("Largest number is:", r)'''