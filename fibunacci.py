

count = 0
nterms = 10
n1 = 1
n2 = 1
while count < nterms:
    print(n1)
    nth = n1 + n2
    #update values

    n1 = n2
    n2 = nth
    count +=1
