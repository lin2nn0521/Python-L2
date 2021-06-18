k=0
p=""
a=int(input())
print("")
for i in range(a):
    
    b=input().split()
    c=int(len(b))
    k=0
    for j in range(c):
        if len(b[j])<j+1-k:
            k=k+1
        else:
            p=p+b[j][j-k]
            
    print(p)


            




