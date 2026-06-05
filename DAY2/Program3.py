num = int(input("Enter a number: "))

product = 1
original_num = num 

num = abs(num)

if num == 0:
    product = 0
else:
    while num > 0:
        digit = num % 10        
        product = product * digit  
        num = num // 10         

print(f"The product of the digits of {original_num} is: {product}")