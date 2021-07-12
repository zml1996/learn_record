def smallestGoodBase(n: str) -> str:
    n=int(n)
    min=n
    for i in range(n, n-60,-1):
        resu=a(n,i,[])
        if resu:
            return i

def a(nn,jz,li):
    #print(nn,jz,li)
    new_nn=nn//jz
    yushu=nn%jz
    if yushu!=1:
        return False
    if new_nn==0:
        li.append(yushu)
        return li
    else:
        li.append(yushu)
        return a(new_nn,jz,li)

resu=smallestGoodBase('4681')
print(resu)
exit(1)

for i in range(100,90,-1):
    print(i)