def cal(andis):
    if andis == 0  or andis == 1:
        return 1
    else:
        return cal(andis - 1) + cal(andis - 2)
    
    
    
andis = int(input('bede???'))

res = cal(andis)

print (res ,' = javab = ')