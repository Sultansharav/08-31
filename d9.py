# 9. n ээс m тоо хүртэлх тэгш бүх тоонуудын тоог ол

n, m = [int(x) for x in input().split()]
for i in range(n, m + 1):
        if i % 2 == 0:
                print(i)