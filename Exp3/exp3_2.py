"""用辗转相除法计算两个正整数的最大公约数及最小公倍数"""
num1, num2 = map(int, input("请输入两个正整数，用空格隔开：").split())
if num1 <= 0 or num2 <= 0:
    exit("请按要求输入正整数！")
product = num1 * num2
while num2 != 0:
    num1, num2 = num2, num1 % num2
print(f"最大公约数为：{num1}\n最小公倍数为：{product // num1}")
