"""""""""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


Definitions

Prime number
    - A prime number is a whole number greater than 1 whose only factors are 1 and itself

"""""""""


num = 4
#prime number are greater than 1
if num > 1:

    # check for factors
    for i in range(2, num):
        if(num % i) == 0:
            print(num, "is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is a prime number")
