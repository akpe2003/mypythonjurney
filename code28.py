def is_prime(n):
	 
	if n <= 1:
		return False
	for i in range(2,n):
		if n % i ==0:
			return False
	return True

print(is_prime(20))
print(is_prime(19))
print(is_prime(49))

"""
primes=[]
for x in range(0,n):
	if is_prime(y):
		primes.append(x)
		
print(f"All the prime numbers all up to {y} are {primes}.")
alternate_prime=primes[::2]
print()
print(f"All the alternate primes are: {alternate_prime}.")
"""		