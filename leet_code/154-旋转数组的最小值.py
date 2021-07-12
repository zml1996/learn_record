'''

'''

def ss(li):
    start=li[0]
    while True:
        if len(li)<10:
            num=li[0]
            print(li,'0000')
            for i in li:
                if i<num:
                    num=i
            return num
        inx=int(len(li)/2)
        nums1=li[inx-1]
        nums2 = li[inx]
        nums3 = li[inx+1]
        if nums1<=nums2<=nums3 and nums3<start:#说明最小值在inx 的左边
            li=li[0:inx]
        elif nums1<=nums2<=nums3 and nums3>start:#
            li = li[inx:]
        elif nums1 <= nums2 <= nums3 and nums3 == start:
            li=li
        else:
            return min(nums1,nums2,nums3)




li=[15,15,15,17,17,1,2,3,4,6,7,8,9,10,11,11,11,14]
num=ss(li)
print(num)
