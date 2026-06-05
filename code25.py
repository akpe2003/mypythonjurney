numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
even_numbers=[]
odd_numbers=[]
y=len(numbers)
for x in range(y):
	if numbers[x] % 2==0:
		even_numbers.append(numbers[x])
	else: 
		odd_numbers.append(numbers[x])
		
print()
print(f"Even numbers: {even_numbers}")
print()
print(f"Odd numbers: {odd_numbers}")