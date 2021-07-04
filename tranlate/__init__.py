import requests
import json

#彩云小译 英译汉
def tranlate(source, direction):
    url = "http://api.interpreter.caiyunai.com/v1/translator"
    #WARNING, this token is a test token for new developers, and it should be replaced by your token
    token = "ru4lh622z08nwhhccorp"
    payload = {
            "source" : source, 
            "trans_type" : direction,
            "request_id" : "demo",
            "detect": True,
            }
    headers = {
            'content-type': "application/json",
            'x-authorization': "token " + token,
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    print(json.loads(response.text)['target'])
    return json.loads(response.text)['target']