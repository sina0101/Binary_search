def test(list1,num1,index_min,index_max):
    
    mind = (index_min+index_max)//2
    
    if list1[mind] == num1 :
        return mind
    
    if list1[mind] > num1:
        return test(list1,num1,index_min,mind-1)
    
    if list1[mind] < num1:
        return test(list1,num1,mind+1,index_max)
    else:
        return -1

num1 = 4
list1 = [4,58,63,14,87]
list1.sort()

index_min = 0
index_max = len(list1)-1
 
res = test(list1,num1,index_min,index_max)

print (res , list1)