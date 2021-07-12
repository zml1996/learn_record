import socket
import threading
import time
def jiankong(li):
    while True:
        print('jiankong循环中',len(li))
        for l in li:
            msg = l.recv(1024)
            print('线程循环获取数据中：',msg.decode('utf-8'))
            if msg is not  None:
                print(msg.decode('utf-8'))
            l.send('接收到客户端数据。返回给你一条。')
        time.sleep(10)




st=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
st.bind(('127.0.0.1',8009))
st.listen(5)
st_li=[]
print('服务端已启动，等待链接.......')
td=threading.Thread(target=jiankong,args=(st_li,))
td.start()
while True:
    con,address=st.accept()#阻塞方法 如果不用多线程的话会阻塞请求
    st_li.append(con)
    msg=con.recv(1024)#按1024去取   可能没取完  需要一直取
    print('哈哈哈哈，连接测试', msg.decode('utf-8'),address)
    print('此时连接数量为:',len(st_li))

