"""编程计算100以内的素数（使用函数）"""


def is_prime(num):
    """判断是否为素数"""
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True


pnlist = [str(num) for num in range(2, 101) if is_prime(num)]
print(*pnlist, sep=',', end='。\n')
print("100以内共有{}个素数。".format(len(pnlist)))
