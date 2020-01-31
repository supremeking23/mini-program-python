# this program will accept user input


num  =int(input("what number:>"))

if num == 0:
    print(num, "is zero")
elif num > 0:
    print(num, "is a postive number")
else:
    print(num, "is a negative number")