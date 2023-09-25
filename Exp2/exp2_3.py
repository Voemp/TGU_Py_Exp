list1 = input("请输入列表元素，多个元素用空格分隔：").split()
print("从短到长输出结果为：" + str(sorted(list1, key=len)))
