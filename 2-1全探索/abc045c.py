# https://atcoder.jp/contests/arc061/tasks/arc061_a
s = input()

n = len(s)

result = 0
for bit in range(2**(n-1)):
    tmp = 0
    cur = 0
    for i in range(n-1):
        if bit >> i & 1:
            tmp += int(s[cur:i+1])
            cur = i+1
    tmp += int(s[cur:])
    result += tmp

print(result)
