#Find all pairs (i, j) such that i + j = 10 within a range:

for i in range(1,11):
    for j in range(1,11):
        if i+j==10:
            print(f"Pair: ({i}, {j})")