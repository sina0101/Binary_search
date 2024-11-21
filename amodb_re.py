def cal(num1 ,num2 ):
    
    if num1 < num2:
        return num1
    if num1 == num2 :
        return 0
    if num1 > num2:
        return cal(num1 - num2 , num2)
    
    
    
num1 = int(input('bede 1 ???'))
num2 = int(input('bede 2 ???')) 

res = cal(num1 , num2)

print (res , '= javab =')