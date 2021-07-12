'''
学习并理解python装饰器中的作用
希望能理解的深一点  记住的时间长一点
装饰器适用范围及情况分析：
1.首先是对于频繁调用，且逻辑相对独立的方法  比如写日志什么的  每个方法开始和结束需要写日志。
2.常用的加解密方法  比如对http请求内容，每一次需要加密或者解密
3.验证登陆   不符合条件的跳转到指定页面。
'''
import time



#不带参数到装饰器
def decrator(func):
    def wrap(*args,**kwargs):
        print(*kwargs)
        #print('参数为:',str(*args),str(**kwargs))
        start_time = time.time()
        res = func(**kwargs)
        end_time = time.time()
        print('运行时间为', end_time-start_time)
        return res
    return wrap  #相当于先返回这个方法  然后 add 给参数时会给到 warp方法参数里 然后相当于调用里warp方法


@decrator
def add(x,y):#定义一个加法方法
    time.sleep(2)
    print('加法:',x,y)

#add(x=1,y=2)



#带参数的装饰器

def args_decrator(params):
    def inner(func):#内层函数  相当于原来的装饰器方法  func代表被装饰器修饰的方法
        def aaaa(*args,**kwargs):
            print('装饰器之前的操作。')
            func(*args,**kwargs)
            print('执行方法之后')
        return aaaa  #必须要返回  要

    def inner2(func):#内层函数  相当于原来的装饰器方法  func代表被装饰器修饰的方法
        def aaaa(*args,**kwargs):
            print('装饰器之前的操作。inner2')
            func(*args,**kwargs)
            print('执行方法之后,inner2')
        return aaaa
    if params==1:
        return inner
    else:
        return inner2

@args_decrator(11)
def ssa():
    print('ss方法')

ssa()








