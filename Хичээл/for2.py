#  i нь зөвхөн тоонд ашиглагддаг.

a = int(input()) # гараас тоо оруулж байгаа /7 = 1 + 2 + 3 + ... + 7
niilber = 0
for i in range (0 , a + 1): # 5   
    niilber = niilber + i
    print(i)
print("a hurtelh toonii niilber:" , niilber) 



# олон параметр оруулж болно. 
a = int(input()) # гараас тоо оруулж байгаа /7 = 1 + 2 + 3 + ... + 7
niilber = 0
for i in range (0 , a + 1): # энд параметруудыг оруулна. 
    niilber = niilber + i
    print(i)
print("a hurtelh toonii niilber:" , niilber) 

# for ийг зогсоохын тулд break -ийг ашиглана.