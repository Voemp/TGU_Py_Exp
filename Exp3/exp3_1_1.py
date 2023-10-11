"""以单重循环方法输出所有水仙花数"""
nnlist = []
for i in range(100, 1000):
    if ((i // 100) ** 3 + ((i // 10) % 10) ** 3 + (i % 10) ** 3) == i:
        nnlist.append(str(i))
print(','.join(nnlist))
