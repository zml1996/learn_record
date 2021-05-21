
'''
优化思路，不要一个一个的加   先按 基准数的 两倍去加 不够了再按一个一个去加。
注意的地方：
关于递归中使用return ，当需要方法返回值时，递归方法前是要加return的。
这个需要再调试调试，加深理解。

'''
class Solution:
    def multiply(self, A: int, B: int) -> int:
        resu=self.ss(A,B,1,A)
        return resu

    #将 乘法切割成加法
    #99*100
    def ss(self,a,b,base,init_a):#b代表剩余未加点   base 代表当前这个数是几倍的基数
        if b>1:
            if b>base:
                new_a=a+a
                new_b=b-base
                new_base=base+base
                return self.ss(new_a,new_b,new_base,init_a)
            else:
                new_a=a+init_a
                new_b=b-1
                new_base=base+1
                return self.ss(new_a,new_b,new_base,init_a)

        return a