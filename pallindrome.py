num = int(input("enter a no.:"))
orginal_num = num   
reverse_num = 0
while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10 
if orginal_num == reverse_num:
    print(orginal_num,"is a pallindrome")
else:
    print(orginal_num,"is not a pallindrome")
    
