# http://poj.org/problem?id=3253
n = int(input())
L = []
for _ in range(n):
    l = int(input())
    L.append(l)

L.sort()
result = 0
while 2 <= len(L):
    tmp = L[0] + L[1]
    result += tmp
    L = L[2:] + [tmp]
    # print(L, result)

print(result)
