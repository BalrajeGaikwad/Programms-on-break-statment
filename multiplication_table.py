for i in range(1, 6):  # Outer loop for rows
    for j in range(1, 6):  # Inner loop for columns
        print(f"{i * j:2}", end=" ")  # Print product with proper spacing
    print()  # Newline after each row
