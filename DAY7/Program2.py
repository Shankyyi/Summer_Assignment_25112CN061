def recursive_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

terms = int(input("Enter the number of terms for the Fibonacci series: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(recursive_fibonacci(i), end=" ")
print()