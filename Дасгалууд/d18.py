# m тоо хүртэл хэдэн анхны тоо байгааг ол

n = int(input())
count = 0
for i in range(2, n + 1):
    k = 0
    for j in range (2, i // 2 + 1):
        if i % j == 0:
            k += 1
    if k == 0:
        print(i)
        count +=1

print(n, "hurtelh anhny toonuudyn too ni: ", count)
