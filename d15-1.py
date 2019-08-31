# Өгөдсөн n тоо анхны тоо мөн үү

n = int(input())
k = 0
for i in range(1,n+1):
    if n%1==0:
        k+= 1
if k == 2:
    print("Yes")
else:
    print("No")