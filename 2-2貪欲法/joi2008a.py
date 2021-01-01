# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_a
import sys
from io import StringIO
import unittest


def resolve():
    num = int(input())
    rest = 1000 - num
    result = 0

    def pay(money, rest, result):
        if rest >= money:
            cnt = rest // money
            rest -= money * cnt
            result += cnt
        return rest, result

    rest, result = pay(500, rest, result)
    rest, result = pay(100, rest, result)
    rest, result = pay(50, rest, result)
    rest, result = pay(10, rest, result)
    rest, result = pay(5, rest, result)
    rest, result = pay(1, rest, result)

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
        input = """380"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """15"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
