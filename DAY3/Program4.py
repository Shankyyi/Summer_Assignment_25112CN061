a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

num1 = a
num2 = b

while b != 0:
    temp = b
    b = a % b
    a = temp

gcd = a

lcm = (num1 * num2) // gcd

print(f"The LCM of {num1} and {num2} is: {lcm}")