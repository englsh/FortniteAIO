import requests,base64,os,json,time
from datetime import datetime

while True:
    try:
        data = json.loads(open(os.path.expandvars("%localappdata%")+"/FortniteAIO/token.json","r").read())
    except:
        exit()

    tkn = base64.b64decode(data['access_token'].encode()).decode('utf-8')

    h={
        "Authorization": f"Bearer {tkn}"
    }
    req = requests.post(f"https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{data['account_id']}/deviceAuth",headers=h)
    data1 = req.json()
    try:
        data1['errorCode']
        exit()
    except:
        h={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE="
        }
        d={
            "grant_type": "device_auth",
            "account_id": data1['accountId'],
            "device_id": data1['deviceId'],
            "secret": data1['secret']
        }
        req = requests.post("https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token",headers=h,data=d)
        data1 = req.json()
        newdata='{'+f'"access_token":"{base64.b64encode(data1["access_token"].encode()).decode("utf-8")}","account_id":"{data1["account_id"]}","account_name":"{data1["displayName"]}"'+"}"
        open(os.path.expandvars("%localappdata%")+"/FortniteAIO/token.json","w").write(newdata)
        time2 = datetime.now()
        print(time2.strftime("%H:%M:%S") + " | RESET TOKEN")
        time.sleep(150)