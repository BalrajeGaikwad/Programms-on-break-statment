"""i = 1
j = 1

while i <= 100:
    i += 1
    while j <= 200:
        j += 1
        if j == 150:
            break
        else:
            print(i, j)
"""

# Stop the loop when the counter reaches 3

counter=0

while True:
    print(f"counter :{counter}")
    if counter==3:
        print("break the loop")
        break
    counter+=1