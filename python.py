# Number of rows for the pattern
rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")  # Print numbers on the same line
    print()  # Move to the next line after each row
