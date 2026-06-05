num = int(input("Enter an integer to reverse: "))

reversed_num = 0
original_num = num  

while num > 0:
    remainder = num % 10                  
    reversed_num = (reversed_num * 10) + remainder 
    num = num // 10                       

print(f"The reversed number is: {reversed_num}")