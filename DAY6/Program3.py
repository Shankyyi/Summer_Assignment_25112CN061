number = int(input("Enter a number: "))

temp = number
count = 0

while temp > 0:
    if temp % 2 == 1:
        count += 1
    temp //= 2

print(f"The number of set bits in {number} is {count}")