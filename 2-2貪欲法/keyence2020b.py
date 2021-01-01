# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b
import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    secs = []
    for _ in range(n):
        x, l = list(map(int, input().split()))
        secs.append((x-l, x+l))

    secs.sort(key=lambda x: x[1])
    sys.stderr.write(str(secs))

    cur = secs[0][0]
    result = 0
    for i in range(n):
        sec = secs[i]
        if sec[0] < cur:
            continue
        cur = sec[1]
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
        input = """4
2 4
4 3
9 3
100 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
8 20
1 10"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
10 1
2 1
4 1
6 1
8 1"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
