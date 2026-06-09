def reverse_number(num, rev=0):
    if num == 0:
        return rev
    else:
        digit = num % 10
        rev = (rev * 10) + digit
        return reverse_number(num // 10, rev)

number = int(input("Enter a number to reverse: "))

if number < 0:
    actual_number = abs(number)
    result = reverse_number(actual_number)
    print(f"The reversed number is: -{result}")
else:
    result = reverse_number(number)
    print(f"The reversed number is: {result}")