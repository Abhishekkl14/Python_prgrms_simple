num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
if '.' in num1 or '.' in num2: 
    sum = float(num1) + float(num2)
    print(sum)
else:
    sum = int(num1) + int(num2)
    print(sum)
