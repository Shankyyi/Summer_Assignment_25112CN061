rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(rows):
        if j < i:
            print(chr(65 + j), end="")
    print()