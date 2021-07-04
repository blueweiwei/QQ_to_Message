import requests
import tranlate

# 地区经纬度
position="113.805536,34.780562"
# 密钥 彩云天气
key="96Ly7wgKGq6FhllM"


#获取地区的天气信息 
def getWeather():
    url="https://api.caiyunapp.com/v2.5/{}/{}/weather.jsonp".format(key,position)
    r = requests.get(url).json()
    data={}
    if r["status"]=="ok":
        data["forecast_keypoint"]=r["result"]['forecast_keypoint']
        skycon=r['result']['realtime']['skycon']
        data["skycon"]=tranlate.tranlate(skycon, "auto2zh")
        data['temperature']=r['result']['realtime']['temperature']
        data['humidity']=r['result']['realtime']['humidity']
    # print(data)
    return data

