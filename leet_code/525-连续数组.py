
def findMaxLength(nums):
    max_nums = 0
    li=[]
    end = max(len(nums) - 2, 1)
    for i in range(0, end, 2):  # 这个i是起点
        j = i
        while True:

            j = j + 2
            if j > len(nums):
                break
            print(i, j)
            if nums[i:j].count(0) == nums[i:j].count(1):

                if j - i > max_nums:
                    #print('更新max_nums:', max_nums, '--->', j - i)
                    max_nums = j - i
                    li=nums[i:j]
    print(li)
    return max_nums

ss=[1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,1,1,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,0]
s=[1,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0]
print(len(s))
print(findMaxLength(s))
