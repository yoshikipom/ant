# https://atcoder.jp/contests/abc079/tasks/abc079_c

def to_num(op):
    if op == "+":
        return 1
    else:
        return -1


abcd = input()
a = int(abcd[0])
b = int(abcd[1])
c = int(abcd[2])
d = int(abcd[3])

result = ''
for op1 in ("+", "-"):
    for op2 in ("+", "-"):
        for op3 in ("+", "-"):
            if a + to_num(op1) * b + to_num(op2) * c + to_num(op3) * d == 7:
                result = str(a) + op1 + str(b) + op2 + \
                    str(c) + op3 + str(d) + '=7'


print(result)
