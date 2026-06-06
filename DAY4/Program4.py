lower = int(input("Enter lower bound of range: "))
upper = int(input("Enter upper bound of range: "))

print(f"Armstrong numbers between {lower} and {upper} are:")

for num in range(lower, upper + 1):
    temp = num
    digits = len(str(num))
    sum_of_powers = 0
    
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** digits
        temp //= 10
        
    if num == sum_of_powers:
        print(num, end=" ")
print()