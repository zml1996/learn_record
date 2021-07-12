import pyspark
from pyspark import SparkContext,SparkConf
conf=SparkConf().setAppName('test').setMaster('local')
sc=SparkContext(conf=conf)
rdd1=sc.textFile('./data/1.txt')#读取单个文件  rdd1.first() 可以查看一行
print(rdd1.first())
rdd2=sc.wholeTextFiles('./data/*.txt')#读取一个目录下的文件   已文件名、内容的形式返回

#print(rdd2.take(2))  take 方法可以从rdd中取出指定条数的元素

#rdd2.saveAsPickleFile('./data/pickle_file') #根据task个数生成对应数目的序列化文件，且每个序列化文件都有文件头
#rdd2.saveAsSequenceFile('./data/sequence_file')  #SequenceFile 是hadoop用来存储二进制形式的 key,value 设计的平面文件 面向行的存储格式
rdd2.saveAsHadoopFile('./data/hadoop_file')
sc.newAPIHadoopFile()


