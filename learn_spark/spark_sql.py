from pyspark.sql import SparkSession
import pyspark
'spark sql 使用SparkSession连接并进行操作'
saprk=SparkSession.builder.master('local').appName('test_spark_sql')\
    .config("spark.some.config.option", "some-value")\
    .getOrCreate()


df=saprk.read.json( './sql_test/pepole.json')#读取文件 按行去解析json 然后相同的字段排列在一起
df.show() #展示数据
df.printSchema()  #显示各个字段及类型
df.select('name').filter(df['age']>20).show()#同 df['name'] df.name  差异是返回的对象类型可能不一样
df.groupBy("age").count().show()

#df.createOrReplaceTempView("people")  另一种视图
df.createGlobalTempView("people")#创建全局的临时视图  能以sql的形式进行查询
saprk.sql('select * from global_temp.people').show()




