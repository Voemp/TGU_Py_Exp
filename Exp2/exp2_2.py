str1 = input("请输入一个字符串：")
print("该字符串" + ("是" if str1 == str1[::-1] else "不是") + "回文串")
