# a ээс b хүртэлх тооний нийлбэр ол
a, b = [int(x) for x in input().split()]
niilber = 0
for i in range (a,b+1):
    print(i)
    niilber = niilber + i
print("niilber", niilber)