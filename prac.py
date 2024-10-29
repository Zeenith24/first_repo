lis1=[22,3,52,4,1,44]
print(lis1)
tar=26
print(tar)

flag=0
x=len(lis1)
for i in range(x):
    for j in range(x):
        if lis1[i]==lis1[j]:
            continue
        else :
            if lis1[i]+lis1[j]==tar:
                print( " pos1 : ",i,"pos2 : ", j)
                flag=1
            else :
                continue
if flag==0:
    print('element does not exsist ') 
                      

