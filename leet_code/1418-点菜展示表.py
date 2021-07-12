'''
orders[i]=[customerNamei,tableNumberi,foodItemi]
'''
[].reverse()
def displayTable(orders):
    title = []  # 放菜名
    dt = []  # 放菜品对应的数量 按行
    table_nums_li = []  # 放桌号

    for ord in orders:
        tableNumber = int(ord[1])
        foodItem = ord[2]
        print(tableNumber,foodItem)
        if tableNumber not in table_nums_li:  # 先判断这个桌号有没有出现过
            table_nums_li.append(tableNumber)
            dt.append([0] * len(table_nums_li))  # 加一行

        if foodItem not in title:
            title.append(foodItem)
            for d in dt:
                d.append(0)

        food_idx = title.index(foodItem)  # 获取菜的下标 第几列
        user_idx = table_nums_li.index(tableNumber)  # 第几行
        dt[user_idx][food_idx] += 1
    new_table_nums_li,new_dt=sort(table_nums_li,dt)
    print(table_nums_li,"_____",dt)
    print(new_table_nums_li,"_____",new_dt)

from copy import copy
def sort(a,b):
    aa=copy(a)
    new_a=sorted(a)
    new_b=[]
    for i in range(len(b)):
        idx=a.index(new_a[i])
        new_b.append(b[idx])
    return new_a,new_b




orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]


displayTable(orders)

