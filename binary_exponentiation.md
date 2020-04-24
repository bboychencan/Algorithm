# Binary Exponentiation (Fast Power)

Calculate a ** n

The idea is very simple, brute force algorithm will have a time complexity of O(n)
We can reduce it to O(log(n)) by applying this information. a ** (11011) = a ** (2**4) * a ** (2**3) * a ** (2**1) * a ** (2**0)
and 2 ** 4 = 2 ** 3 * 2, 2 ** 3 = 2 ** 2 * 2

```python
def fast_power(a, n):
	if n == 0: return 1
	res = 1
	while n > 0:
		if n & 1 == 1:
			res *= a
		a = a * a
		n = n >> 1
	return res
```

