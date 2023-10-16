"""求20-100之间的素数并输出个数"""
pnlist = [str(num) for num in range(20, 101) if all(num % i != 0 for i in range(2, num // 2 + 1))]
print(*pnlist, sep=',')
print("素数个数为：%s" % len(pnlist))
