# https://atcoder.jp/contests/abc054/tasks/abc054_c
import sys
from io import StringIO
import unittest
import itertools


def resolve():
    n, m = list(map(int, input().split()))
    d = [[False for j in range(n)] for i in range(n)]
    for _ in range(m):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        d[a][b] = True
        d[b][a] = True

    result = 0
    for perm in list(itertools.permutations(range(n))):
        if perm[0] != 0:
            continue
        for i in range(n-1):
            if not d[perm[i]][perm[i+1]]:
                break
        else:
            result += 1

    print(result)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3 3
1 2
1 3
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
