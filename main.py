a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
operator = input("Select the operator: \nPress + for addition \n- for subtraction \n* for multiplication \n/for "
                 "division \n% for remainder \n** for exponent \n")
if operator == '+':
    sum = round((a + b), 2)
    print(f"Sum = {sum}")
elif operator == '-':
    difference = round((a - b), 2)
    print(f"Difference = {difference}")
elif operator == '*':
    product = round((a * b), 2)
    print(f"Product = {product}")
elif operator == '/':
    if b == 0:
        print("Zero Error: divided by zero")
    else:
        quotient = round((a/b), 2)
        print(f"Quotient = {quotient}")
elif operator == '%':
    remainder = round((a % b), 2)
    print(f"Remainder = {remainder}")
elif operator == '**':
    power = round((a**b))
    print(f"Power = {power}")
else:
    print("Invalid Operator")
