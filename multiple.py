#multiple of 3 or 5
print("ivan")
total = 0

for i in range(1,10):
    if i % 3 == 0:
        print(i, " is a multiple of 3")
        total += i
    if i % 5 == 0:
        print(i, " is a multiple of 5")
        total += i


print(total)