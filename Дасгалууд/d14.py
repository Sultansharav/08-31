# Өгөдсөн n тоо анхны /prime nubmer/ тоо мөн үү?
# анхны тоо гэж зөвхөн 1 болон өөртөө хуваагддаг эерэг тоог хэлнэ

'''
num = 11
  
# If given number is greater than 1 
if num > 1: 
      
   # Iterate from 2 to n / 2  
   for i in range(2, num//2): 
         
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number") 
'''


n = int(input())
  
if n > 1: 
   for i in range(2, n // 2): 
       if (n % i) == 0: 
           print(n, "бол анхны тоо биш") 
           break
   else: print(n, "бол анхны тоо мөн")  
else:    print(n, "бол анхны тоо биш") 