import time
import sendSMS,weather

qq="3151351506"
nowDate=time.strftime("%Y-%m-%d %H:%M", time.localtime()) 


# 组装消息 发送消息
def sendWeatherMsg():
    data=weather.getWeather()
    msg='''======{}======
播报今天的天气情况：
天气：{}
温度：{}
湿度：{}
温馨提醒：{}
=========天气播报========='''.format(nowDate,data['skycon'],data['temperature'],data['humidity'],data['forecast_keypoint'])
    sendSMS.postData("3151351506",msg)

if __name__ == '__main__':
    # postData(qq,msg)
    # getWeather(position)
    sendWeatherMsg()
    
def handler (event, context):
    sendWeatherMsg()