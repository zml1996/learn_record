'''
快排
思路：
首先选取中间的一个数
然后左边集合遍历，将所有比这个数大的数放到右边集合里
右边集合也一样到逻辑

然后将子集和也这样走一遍
直到没有元素发生变化
'''

def quick_sort(li):
    nums=0#记录发生变化的次数
    midd=int(len(li) / 2)
    print(li,midd)
    middle=li[midd]
    left=[]
    right=[]
    if len(li)==2:
        if li[0]>li[1]:
            return [li[1],li[0]]
        else:
            return li
    for i in range(0,midd):#左边部分遍历
        print(li[i],middle,li[i]<=middle)
        if li[i]<=middle:
            left.append(li[i])
        else:
            right.append(li[i])
            nums+=1

    for i in range(midd,len(li)): #右边部分遍历
        print(li[i], middle, li[i] <= middle)
        if li[i]<=middle:
            left.append(li[i])
            nums+=1
        else:
            right.append(li[i])


    if nums==0 or len(li)<=1:
        return li
    else:
        if left!=[]:
            print('left:',left)
            left=quick_sort(left)
        if right!=[]:
            print('right:', right)
            right = quick_sort(right)
        return left+right



ss=[2,3,4,1,5,8,0,1020,20,99,67,34,2,2,99]
ss=quick_sort(ss)
print(ss)











