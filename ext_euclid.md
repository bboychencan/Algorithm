# Extended Euclidean
Bezout Lemma
ax + by = gcd(a, b)

To get x, y
We use the same strategy of Euclidean way to get gcd(a, b)
The only difference is that in addition to the original procedure, we keep track 
of s, t
s0 = 1, s1 = 0, t0 = 0, t1 = 1
si+1 = si-1 - qisi, ti+1 = ti-1 - qiti


```python
import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter

def test_case():
	pass

def ext_euclid(a, b):
	r1, r2 = a, b
	s1, s2 = 1, 0
	t1, t2 = 0, 1
	while r2 != 0:
		q = r1 // r2
		r1, r2 = r2, r1 - q * r2
		s1, s2 = s2, s1 - q * s2
		t1, t2 = t2, t1 - q * t2
	return s1, t1, r1

def gcd(a, b):
	while b != 0:
		t = a % b
		a = b
		b = t
	return a

def main():
    a, b = list(map(int, input().split()))
    print(gcd(a, b))
    print(ext_euclid(a, b))

if __name__=="__main__":
	main()
```