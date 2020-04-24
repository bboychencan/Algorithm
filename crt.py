

n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]

for i in range(n):
    a[i], b[i] = list(map(int, input().split()))

total = 1

for i in range(n):
     total *= a[i]

m = [0 for i in range(n)]
for i in range(n):
     m[i] = total // a[i]

def extgcd(x, y):
     old_r, r = x, y
     old_s, s = 1, 0
     old_t, t = 0, 1
     if r == 0:
         return 1, 0, old_r
     else:
         while r:
             q = old_r // r
             old_r, r = r, old_r - q * r
             old_s, s = s, old_s - q * s
             old_t, t = t, old_t - q * t
         return old_s, old_t, old_r

# print(a, b, m)
res = 0
for i in range(n):
     s, t, r = extgcd(m[i], a[i])
     s = (s + a[i]) % a[i]
     # print(m[i], a[i], s, t, r, s*m[i]*b[i])
     res = res + s * m[i] * b[i]
     
print(res % total)