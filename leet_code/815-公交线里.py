
'''
输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
输出：-1

'''
from typing import List
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        target_list=[]
        for i in  range(routes):
           if target in routes[i]:
               target_list.append(i)
        for j in target_list:
            rou_=routes[j]
            for jj in rou_:
                if jj==target:continue
                for ii in range(routes):
                    if ii in target_list:continue
                    ii_tar=target[ii]
                    if jj in ii_tar:#说明这个车经过里别的车站 遍历剩下的车站
                        pass



