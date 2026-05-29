def Calculate_Values():
    number1=input("Please enter the value for the first number here: ")
    number1=int(number1)
    print()
    number2=input("Please enter the value for the second number here: ")
    number2=int(number2)
    product=number1*number2
    sum=number1+number2
    print()
    if product <= 1000:
        return f"The result is: {product}"
    else:
        return f"The result is: {sum}"
        
        
print(Calculate_Values())