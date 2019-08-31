# 6. a тоог b зэрэгт дэвшүүл
# 2 ** 5 = 32   = 2 * 2 * 2 * 2 * 2 

a, b = [int(x) for x in input().split()]
res = 1
for i in range (b):
    res = res * a
print("хариу", res)
