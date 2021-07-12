import readline

from pyspark import SparkContext
from pyspark import SparkConf

def test(a,b):
    print(a,b)
    return int(a)+int(b)

conf=SparkConf().setAppName('test').setMaster('local')
sc=SparkContext(conf=conf)
src_dt=sc.textFile('./data/1.txt')
new_dt=src_dt.map(lambda line:line.strip().split('  '))
for i in new_dt.collect():
    print(i)
new_dt2=new_dt.reduceByKey(test)
print(new_dt2.collect())

# print(new_dt2.collect())



