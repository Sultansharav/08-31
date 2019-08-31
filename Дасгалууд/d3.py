# 3. n ээс m тоо хүртэлх тэгш тооны нийлбэр ол

n, m = [int(x) for x in input().split()]
niilber = 0
for i in range (n,m+1):
    if i % 2 == 0:
        print(i)
        niilber = niilber + i
print("niilber" , niilber)