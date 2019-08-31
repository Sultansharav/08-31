# 7. a болон b тооны үржвэр ол                  # 5 * 3 = 15    = 5 + 5 + 5

a, b = [int(x) for x in input().split()]
res = 0
for i in range (b):
    res = res + a
print ("хариу: ", res)
