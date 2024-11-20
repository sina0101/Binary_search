def test(list1,num1):
    list1.sort()
    andis_max = len(list1)-1
    andis_min = 0
    
    
    
    while (andis_max >= andis_min):
        mind = (andis_max + andis_min)//2    
        if list1[mind] == num1:
            
            return mind
        
        
        if list1[mind] > num1 :
             andis_max = mind -1
            
    
        if list1[mind] < num1 :
            andis_min = mind +1 
        
        
list1 = [4,58,63,14,87]
num1 = 87

list1.sort()

res = test(list1, num1)
print (res , list1)