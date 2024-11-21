def fuck(num1):
    if num1 == 1 or num1 == 0:
        return num1
    
    
    else:
        return num1 * fuck(num1 -1)
    
    
    
    
num1 = int(input('bede???'))

res = fuck(num1)

print (res ,'=javab=')