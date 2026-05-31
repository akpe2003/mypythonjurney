def palindrome(number_string):
    new_number=str(number_string)
    that_number=new_number[::-1]
    if that_number==new_number:
        print(f"The number you entered which is: {number_string} is a palindrome.")
    else:
        print(f"The number you entered which is: {number_string} is not a palindrome.")
		
palindrome(121)
print()
palindrome(125)