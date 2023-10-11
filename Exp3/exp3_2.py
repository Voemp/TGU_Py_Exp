"""用辗转相除法计算两个正整数的最大公约数及最小公倍数"""
numlist = input("请输入两个正整数，用空格隔开：").split()
num1, num2 = int(numlist[0]), int(numlist[1])
if num1 <= 0 or num2 <= 0:
    print("请按要求输入正整数！")
    exit(0)
while num2 != 0:
    num1, num2 = num2, num1 % num2
print("最大公约数为：%d" % num1)
print("最小公倍数为：%d" % (int(numlist[0]) * int(numlist[1]) / num1))
