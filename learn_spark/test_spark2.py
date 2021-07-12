import time

from pyspark import SparkContext,SparkConf

#-----------------------------------------------
#spark map reduce练习
def mymap(line):
    return len(line)

#在spark中这样对数字进行叠加是不可行对  由于闭包机制，每一份机器上都单独有一份所引用都对象 应该使用saprk提供都累加器
nums_all=0
def test_foreach(nums):
    global nums_all
    nums_all+=nums
    print(nums_all)




if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local')
    sc = SparkContext(conf=conf)

    text_rdd=sc.textFile('./data/*.txt')
    map_rdd=text_rdd.map(mymap)
    #count=map_rdd.foreach(test_foreach)
    # new_text_rdd=text_rdd.flatMap(lambda x:(x,'hahaha','xxxx'))
    new_rdd=text_rdd.map(lambda line:line.split('\t'))
    print(new_rdd.first())
    time.sleep(10000)
    # for i in map_rdd.take(5):
    #     print(i)
    #rdd2 = sc.textFile('./data/sequence_file', )  # 读取一个目录下的文件   已文件名、内容的形式返回
    #print(rdd2.first().encode('utf-8').decode())

