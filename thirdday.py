''''# conditional statements
a = 33
b = 20
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")




# traffic light
light = input("light: ")
if light == "red":
    print("stop")
elif light == "green":
    print("go")
elif light == "yellow":
    print("look")
else:
    print("light is broken")

 # grade



#single line if / Ternary operator
food = input("food: ")
eat = "yes" if food == "apple" else "no"
print(eat)


food = input("food: ")
print("sweet")if food == "mango" or food == "coconut" else print("not sweet")

# clever if /ternary operator

sale = float(input("sale: "))
tax = sale * (0.2 if sale >= 1000 else 0.1)
print(tax)


# check even or odd
num = int(input("num: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")'''


num = int(input("num: "))
if (num % 2) == 0:
    if (num == 10):
        print("yes print")
    else:
        print("even")
else:
    print("odd")


# 
#  greatest of three numbers

a = int(input("a: "))
b = int(input("b: "))   
c = int(input("c: "))
if a>=b  & a>c:
    print("a is greatest")
elif b>=a & b>c:
    print("b is greatest")
else:
    print("c is greatest")


    # check for multiple of 7
    num = int(input("num: "))
    if num % 5 ==0:
        print("multiple of 7")
    else:
        print("not a multiple of 7")