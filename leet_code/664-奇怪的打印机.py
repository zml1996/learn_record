'''

有台奇怪的打印机有以下两个特殊要求：

打印机每次只能打印由 同一个字符 组成的序列。
每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。

输入：s = "aaabbb"
输出：2
解释：首先打印 "aaa" 然后打印 "bbb"。
'''


def strangePrinter(s):
    flag = ''  # 代表上一个数
    nums = 1
    sn_li = []
    for i in range(len(s)):
        if s[i] == flag:
            nums += 1
        else:
            if nums > 1:
                sn_li.append(flag * nums)
                nums = 1
            else:
                if flag=='':
                    flag = s[i]
                    continue
                sn_li.append(flag)
            flag = s[i]
    sn_li.append(flag*nums)
    print(sn_li)
    #对于打印



strangePrinter('aaaaccaabbbbbbbbbccaa')




