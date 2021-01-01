# https://atcoder.jp/contests/abc104/tasks/abc104_c
import math
d, g = list(map(int, input().split()))
pcs = []
for i in range(d):
    p, c = list(map(int, input().split()))
    point = (i+1) * 100
    pcs.append((point, p, c))

# print(pcs)
result = float('inf')
for bit in range(2**d):
    tmp = 0
    tmp_cnt = 0
    unused_max = -1
    for i in range(d):
        if bit >> i & 1:
            tmp += pcs[i][0] * pcs[i][1] + pcs[i][2]
            tmp_cnt += pcs[i][1]
        else:
            unused_max = i

    if unused_max != -1 and tmp < g:
        if pcs[unused_max][0] * pcs[unused_max][1] + tmp < g:
            continue
        tmp_cnt += math.ceil((g-tmp)/pcs[unused_max][0])

    # print(bin(bit), tmp_cnt)
    result = min(result, tmp_cnt)

print(result)
