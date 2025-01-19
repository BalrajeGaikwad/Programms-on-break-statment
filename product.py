
# Find the first pair of numbers (i, j) whose product is greater than 50
found = False
for i in range(1, 11):
    for j in range(1, 11):
        if i * j > 50:
            print(f"Breaking at i={i}, j={j}")
            found = True
            break
    if found:
        break
