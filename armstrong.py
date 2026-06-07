num = int(input("enter a no.:"))
original_num =num
digits =len(str(num))

sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit ** digits
    num = num // 10

if original_num == sum_of_digits:
    print(original_num,"is an armstrong no.")
else:
    print(original_num,"is not an armstrong no.")
    
