# https://atcoder.jp/contests/abc076/tasks/abc076_c
import sys
from io import StringIO
import unittest


def resolve():
    s = input()
    t = input()
    s = [c for c in s]
    t = [c for c in t]
    for i in range(len(s)-len(t), -1, -1):
        # print(i)
        for j in range(len(t)):
            # print(s[i+j], t[j])
            if s[i+j] != t[j] and s[i+j] != '?':
                break
        else:
            s[i:i+len(t)] = t[:]
            s = ''.join(s)
            s = s.replace('?', 'a')
            print(s)
            break
    else:
        print('UNRESTORABLE')


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
        input = """?tc????
coder"""
        output = """atcoder"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """??p??d??
abc"""
        output = """UNRESTORABLE"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
