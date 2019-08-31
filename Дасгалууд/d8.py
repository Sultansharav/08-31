# print all odd Numbers in range
# энэ арга нь эхлэхээс төгсгөл хүртэлх бүх 
# сондгой тоонуудыг нэг шугам дотор харуулна

'''  
start, end = 1, 15
  
for num in range(start, end + 1): 
    if num % 2 != 0: 
        print(num, end = " ")
'''

# n ээс m тоо хүртэлх сондгой бүх тоонуудыг хэвлэ

n, m = [int(x) for x in input().split()]
for i in range(n, m + 1):
        if i % 2 == 1:
                print(i)