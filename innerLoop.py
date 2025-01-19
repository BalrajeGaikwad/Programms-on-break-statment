for i in range(1,4):
    for j in range(1,4):
        if j==2:
            print(f"Breaking inner loop at i ={i} j={j}")
            break
        print(f"i={i} j={j}")