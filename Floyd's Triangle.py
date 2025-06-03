rows = int(input("Enter the row size for the pattern: "))
num = 1
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        print(num, end=" ")  # Print numbers in sequence
        num += 1
    print()

   #0 and 1 triangle

    rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(rows  - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, 2 * i):  # Inner loop for stars
        if k == 1 or k == 2 * i - 1 or i == rows:  # Print star on borders
            print("0", end=" ")
        else:
            print("1", end=" ")  # Print space inside
    print()