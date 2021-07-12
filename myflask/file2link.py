'''
reres替换本地文件有问题  起一个端口用http试一试
'''

from  flask import Flask
app = Flask(__name__)

@app.route("/udc.js")
def udc():
    fill=open('/Users/xiaodu/Desktop/udc2.js','r',encoding='utf-8')
    js_dt=fill.read()
    return js_dt


if __name__ == '__main__':
    app.run()

