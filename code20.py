number=121
original_number=121
reversed_number=0
while number>0:
	digit=number%10
	reversed_number=reversed_number * 10 + digit
	number=number//10
	
is_palindrome=reversed_number==original_number
print(f"Is {original_number} a palindrome?: {is_palindrome}.")