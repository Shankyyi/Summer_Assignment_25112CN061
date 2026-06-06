n = int(input("Enter the position (n) to find the nth Fibonacci number: "))

if n <= 0:
    print("Please enter a positive integer greater than 0.")
elif n == 1:
    print("The 1st Fibonacci number is 0")
elif n == 2:
    print("The 2nd Fibonacci number is 1")
else:
    n1 = 0
    n2 = 1
    for i in range(3, n + 1):
        nth = n1 + n2
        n1 = n2
        n2 = nth
    print(f"The {n}th Fibonacci number is {n2}")