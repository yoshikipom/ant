# https://atcoder.jp/contests/atc001/tasks/dfs_a

import sys
sys.setrecursionlimit(1000000)

h, w = list(map(int, input().split()))
C = []
all_wall_row = ['#'] * (w + 2)
C += [all_wall_row]
for _ in range(h):
    row = input()
    tmp = []
    for c in row:
        tmp += [c]
    tmp = ['#'] + tmp + ['#']
    C.append(tmp)
C += [all_wall_row]

start = (-1, -1)
for i in range(h+2):
    for j in range(w+2):
        if C[i][j] == 's':
            start = (i, j)
            break

# for row in C:
#     print(*row)
# print(start)


def dfs(i, j):
    # print(i, j)
    if C[i][j] == 'g':
        print('Yes')
        exit()
    if C[i][j] == '#':
        return
    C[i][j] = '#'

    vecs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for vec in vecs:
        dfs(i+vec[0], j+vec[1])


dfs(*start)
print('No')
