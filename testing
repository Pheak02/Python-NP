
# 1. Write a Python Program to print Prime Numbers between 2 numbers
amount = 0
for num in range (100 , 201):
    if all(num%i!=0 for i in range (2,num)):
        # print(num)
        amount = amount + 1
print(amount)

# 1a. Write a Python Program to print how many Prime Numbers between 2 numbers
# and using for/else

amount = 0
for num in range (100 , 201):
    for i in range (2,num):
        if (num%i==0):
            break
    else:
        print(num)
        amount = amount + 1
print(amount)

# 1a. Write a Python Program to print how many Prime Numbers between 2 numbers
# and not using for/else
amount = 0
prime = True
for num in range (100 , 201):
    for i in range (2,num):
        if (num%i==0):
            prime = False
            break
    if(prime):
        print(num)
        amount = amount + 1

    prime = True

print(amount)
