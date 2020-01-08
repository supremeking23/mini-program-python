"""""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""""

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