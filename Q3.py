from random import randint 
from math import log 
# Name: Justin Huynh
# Student Number: 7745112
# Class: CSI4108 Cryptography

# Question 3
# Implement the Miller-Rabin probabilistic primality testing algorithm to find a 15-bit integer
# that is probably prime with confidence t = 4.  (Actually implement the Miller-Rabin algorithm; 
# don’t just call it from some library or toolkit.)  Is your “probable prime” in this table:
# https://primes.utm.edu/lists/small/10000.txt ? 

def test(n):
	# Find integers k, q, with k > 0, q odd, such that (n - 1 = (2^k)q)
	# (n - 1)/2^k = q
	q = 0
	k = 0
	for _k in range(1, n):#int(log(n,2)) + 1):
		if ((n - 1) / pow(2,_k)) % 2 == 1:
			q = int(((n - 1) / pow(2,_k)))
			k = _k
			print(k, q)
			break 
			
#	for _k in range(1, n): # int(log(n,2))
#		for _q in range(1, n, 2): # pow(2
#			if n - 1 == pow(2, _k)*_q:
#				q = _q
#				k = _k
#				print(k, q)
#				break
				
	if (k, q) == (0, 0):
		return "composite"

	# Select a random integer a, 1 < a < n -1
	a = randint(2, n - 2)
	
	# if (a^q)mod n = 1 then return ("inconclusive")
	if pow(a, q) % n == 1:
		return "inconclusive"
		
	for j in range(0, k - 1):
		if pow(a, pow(2, j) * q) % n == n - 1:
			return "inconclusive" # n may or may not be a prime 
	return "composite" # n is not a prime 

	