"""使用辗转相除法求两个正整数的最大公约数与最小公倍数（用两个函数来实现，且后者调用前者）"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


num1, num2 = eval(input("请输入两个正整数，用“,”隔开："))
print(f"{gcd(num1, num2)} {lcm(num1, num2)}")
