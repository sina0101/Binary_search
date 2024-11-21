def fuck(num1 ,num2):
    if num2 == 0 :
        return 1
    if num2 == 1 :
        return num1
    if num2 != 1 and num2 != 0:
        return num1 * fuck(num1, num2 -1 )
        
        
        
num1 = int(input('bede 1 ???'))
num2 = int(input('bede 2 ???'))

res = fuck(num1, num2)  
print (res , '=javab=')