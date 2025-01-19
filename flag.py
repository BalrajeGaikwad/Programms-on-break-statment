
# Using a flag to break out of nested loops
found = False
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            print(f"Breaking all loops at i={i}, j={j}")
            found = True
            break
    if found:
        break
