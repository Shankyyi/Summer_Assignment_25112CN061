a = int(int(input("Enter first number: ")))
b = int(int(input("Enter second number: ")))

original_a = a
original_b = b

while b != 0:
    temp = b
    b = a % b
    a = temp

print(f"The GCD of {original_a} and {original_b} is: {a}")