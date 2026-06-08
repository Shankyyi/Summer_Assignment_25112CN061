decimal_num = int(input("Enter a decimal number: "))

if decimal_num == 0:
    print("The binary equivalent is: 0")
else:
    temp = decimal_num
    binary_str = ""
    
    while temp > 0:
        remainder = temp % 2
        binary_str = str(remainder) + binary_str
        temp //= 2
        
    print(f"The binary equivalent of {decimal_num} is {binary_str}")