'''
the prime_number function contains a for loop that demonstrates a 
linear execution time O(n) while the other lines of code taking up
a constant execution time O(1), 
hence 
	O(n) + O(1)
	O(n+1)
translates to another variable lets call it x
	O(n+1 = x)
	O(x)
and since x stands for varible value we can simply replace it with n
hence O(n)
'''
def prime_number(n):
	if n == 1:
		print('1 is a prime number')
		return False

	for x in range(2, n):
		if n%x == 0:
			return False

	print n, 'is a prime number'
	return True

'''
This block of code get_prime_numbers_in_range implements a linear 
execution time O(n). This means that when the prime number range increases, 
the execution time also increases.
'''
def get_prime_numbers_in_range(n):
	for x in range(1, n):
		prime_number(x)

'''
ultimately, since get_prime_numbers_in_range(n) with a linear complexity
calls prime_number(n) which also has a linear complexity results in a function
	O(n*n)
	O(n^2)
'''
if __name__ == "__main__":
	get_prime_numbers_in_range(15)