m="......."

coded=[]
for i in range(len(m)-1):
    k=''
    n=list(m)
    n[i],n[i+1]="-","-"
    coded.append(k.join(n))
print(coded)
