def is_prime(n):
	 
	if n <= 1:
		return False
	for i in range(2,n):
		if n % i ==0:
			return False
	return True

primes=[]
def my_limit(limit):
    for x in range(0,limit):
        if is_prime(x)== True:
            primes.append(x)
    print(f"All the prime numbers all up to {limit} are {primes}.")
    alternate_prime=primes[ : : 2 ]
    print(f"All the alternate primes are: {alternate_prime}.")

my_limit(20)