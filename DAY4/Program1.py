terms = int(input("Enter the number of terms for the Fibonacci series: "))

n1 = 0
n2 = 1
count = 0

if terms <= 0:
    print("Please enter a positive integer.")
elif terms == 1:
    print("Fibonacci series up to 1 term:")
    print(n1)
else:
    print("Fibonacci series:")
    while count < terms:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
print()