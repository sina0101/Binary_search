def tow(n,a,b,c):   
    if n == 1:
        c = a
        
        exit
    else:
        tow(n-1 ,a ,c ,b) 

        c = a
        
        tow(n-1, b, a, c)