def multiply(num1: str, num2: str) -> str:
    print(int(num1)*int(num2))
    if num1 == '0' or num2 == '0':
        return '0'
    jin_nums = 0
    nums_list = []  # 存放所有想加的结果
    # nn1=list(num1)
    # nn1.reverse()
    # nn2=list(num2)
    # nn2.reverse()
    for i in range(len(num1)-1,0,-1):
        print('-------')
        nums = []
        for j in range(len(num2)-1,0,-1):
            ss = int(num1[i]) * int(num2[j]) + jin_nums
            jin_nums=0
            if ss >= 10:
                jin_nums = ss // 10
            ss = ss % 10
            nums.append(ss)

        if jin_nums!=0:
            nums.append(jin_nums)
            jin_nums=0

        nums.reverse()
        nums_list.append(nums)
        print(nums)
    nums_sum='0'
    count=0
    for nums in nums_list:
        nums=nums+['0']*count
        nums_sum=str_add(nums_sum,nums)
        count+=1
    return nums_sum

def str_add(s1,s2):
    # s1=list(s1)
    # s2=list(s2)
    # s1.reverse()
    # s2.reverse()
    if len(s1)>len(s2):
        min_s=s2
        max_s=s1
    else:
        min_s = s1
        max_s = s2
    new_s=[]
    jin=0
    for i in range(len(max_s)-1,0,-1):
        if i<len(min_s):
            mi = 0
        else:
            mi = min_s[i]
        ma=max_s[i]
        he=int(mi)+int(ma)+jin
        if he>=10:
            jin=1
            he-=10
        else:
            jin=0
        new_s.append(str(he))
    if jin!=0:
        new_s.append(str(jin))
    new_s.reverse()
    return ''.join(new_s)


s1="123123"
s2="123"

#print(multiply(s1,s2),'-')
str_add('1024','998')