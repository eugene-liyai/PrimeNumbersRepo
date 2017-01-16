def prime_number(n):
	if n == 1:
		print('1 is a prime number')
		return False

	for x in range(2, n):
		if n%x == 0:
			return False

	print n, 'is a prime number'
	return True

def get_prime_numbers_in_range(n):
	for x in range(1, n):
		prime_number(x)

if __name__ == "__main__":
	get_prime_numbers_in_range(15)