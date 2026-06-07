number = int(input("Enter a number to find its largest prime factor: "))

temp = number
largest_prime_factor = 1

i = 2
while i * i <= temp:
    while temp % i == 0:
        largest_prime_factor = i
        temp //= i
    i += 1

if temp > 1:
    largest_prime_factor = temp

print(f"The largest prime factor of {number} is {largest_prime_factor}")