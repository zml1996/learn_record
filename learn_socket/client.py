
import socket

import time
st=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
st.connect(('127.0.0.1',8009))
nums=1
while True:
    st.send(str('你好，服务端，我是客户端1。第%d条'%nums).encode())
    nums+=1
    time.sleep(5)




