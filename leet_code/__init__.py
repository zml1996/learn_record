def convertToTitle(columnNumber: int) -> str:
    s=''
    while True:
        nums = columnNumber // 26
        print(nums,s)
        if nums>26:
            columnNumber=nums
            s+='Z'
            continue
        else:
            ss=columnNumber%26
            return chr(64+nums)+chr(64+ss)


#"FXSHRXW"
print(convertToTitle(2147483647))