# import re
# from simhash import Simhash, SimhashIndex
# data=[
# '小明你好，今天天气很好a',
# '小明你好，今天天气很好呢',
# '小明你好，今天天气很好呀',
# '小明你好，今天天气很好的',
# '小明你好，今天天气很好吗',
# ]
# sim_li=[]
# nums=1
# for i in data:
#     sim_li.append((nums,Simhash(i)))
#     nums+=1
# index=SimhashIndex(sim_li,k=3)
# ss=index.get_near_dups(Simhash('小明你好，今天天气很好吗呀'))
# print(ss)
