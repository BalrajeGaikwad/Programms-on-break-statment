# Program to find the first number divisible by 7 in a list

num=[3,6,89,3,57,56,7]

for i in num:
    if i%7==0:
        print("first number is : ", i)
        break
