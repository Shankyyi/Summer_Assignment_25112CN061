number = int(input("Enter a number to check: "))

if number <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    divisor_sum = 0
    
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
            
    if divisor_sum == number:
        print(f"{number} is a Perfect number.")
    else:
        print(f"{number} is not a Perfect number.")