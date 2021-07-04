import requests

# qmsg 请求密码地址
host="https://qmsg.zendee.cn/send/0380866be979f52faee6bf44d8d43393"

#发送消息 qq：通知qq号码；msg：推送消息
def postData(qq,msg):
    data={
        'qq':"{}".format(qq),
        'msg':"{}".format(msg)
    }
    r = requests.post(host, data=data)
    print(r)