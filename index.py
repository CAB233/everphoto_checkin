# encoding:utf-8
import requests
import json
#import Demjson
def start():
    header = {    }
    url = "https://api.everphoto.cn/users/self/checkin/v2"
    urllogin = "https://web.everphoto.cn/api/auth"
    #https://api.everphoto.cn/auth/qq/check_registered
    #https://web.everphoto.cn/api/auth
    loginkey = "mobile=+86手机号码" + "&password=密码"
    responselogin=requests.post(urllogin,data=loginkey,headers=header)
    logindata = json.loads(responselogin.text)["data"]
    header["authorization"] = "Bearer "+logindata["token"]
    response=requests.post(url,headers=header)
    datas = json.loads(response.text)
    #print(datas)
    #print("签到状态:",datas['data']['checkin_result'])
    #print("签到天数:",datas['data']['continuity'])
    checkin_result = datas['data']['checkin_result']
    continuity = datas['data']['continuity']
    
    api = "https://sctapi.ftqq.com/    server酱sendkey    .send?title=时光相册签到&desp=messagecontent"
    title = "时光相册"
    content = "是否为今日第一次签到:" + "\n" + str(checkin_result)+ "\t"+ "\t"+ "\n"+ "\n" + "累积签到天数:" + "\n" + str(continuity)
    data1 = {
       "text":title,
       "desp":content
    }
    req = requests.post(api,data = data1)
def main_handler(event, context):
  return start()
if __name__ == '__main__':
  start()

