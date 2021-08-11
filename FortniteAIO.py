def main():
  import os, time,ctypes, requests,json, base64, shutil
  from colorama import Fore
  from requests.api import head

  mural = Fore.MAGENTA+'''
   ______ _   _          _____ ____  
  |  ____| \ | |   /\   |_   _/ __ \ 
  | |__  |  \| |  /  \    | || |  | |
  |  __| | . ` | / /\ \   | || |  | |
  | |    | |\  |/ ____ \ _| || |__| |
  |_|    |_| \_/_/    \_\_____\____/ 

                                                  
  '''+Fore.RESET

  version = "1"
  ctypes.windll.kernel32.SetConsoleTitleW(f"FortniteAIO v{version}")
  os.system("clear || cls")
  print(mural)
  hasLoggedin = False
  #options
  if os.path.exists(os.path.expandvars("%localappdata%")+"/FortniteAIO"):
    hasLoggedin = True
    print(f"{Fore.RESET}[{Fore.MAGENTA}+{Fore.RESET}] Token found!")
    time.sleep(.5)
  else:
    hasLoggedin = False
    print(f"{Fore.RESET}[{Fore.MAGENTA}+{Fore.RESET}] to login, goto 'https://www.epicgames.com/id/login?redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Fid%2Fapi%2Fredirect%3FclientId%3D3446cd72694c4a4485d81b77adbb2141%26responseType%3Dcode%0A'\n")
    print(f"[{Fore.MAGENTA}+{Fore.RESET}] Please enter the code after the '?code=' part ")
    os.mkdir(os.path.expandvars("%localappdata%")+"/FortniteAIO")
    code = input(f"\n[{Fore.MAGENTA}!{Fore.RESET}] ")
    

  print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Logging in...")
  time.sleep(.3)
  if hasLoggedin == False:
    data = {
      "grant_type":"authorization_code",
      "code": code
    }
    headers={
      "Content-Type": "application/x-www-form-urlencoded",
      "Authorization": "basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE="
    }
    authreq = requests.post(f"https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token",headers=headers,data=data)
    acstkn = authreq.json()['access_token']
    acstid = authreq.json()['account_id']
    acstnm = authreq.json()['displayName']
    json1 = '{'+f'"access_token":"{base64.b64encode(acstkn.encode()).decode("utf-8")}","account_id":"{acstid}","account_name":"{acstnm}"'+"}"
    c11 = open(os.path.expandvars("%localappdata%")+"/FortniteAIO/token.json","w")
    c11.write(json1)
    c11.close()
  else:
    c11=open(os.path.expandvars("%localappdata%")+"/FortniteAIO/token.json","r")
    aaaaaaaaaaaaa = json.loads(c11.read())
    c11.close()
    acstkn = base64.b64decode(aaaaaaaaaaaaa['access_token'].encode()).decode('utf-8')
    acstid = aaaaaaaaaaaaa['account_id']
    acstnm = aaaaaaaaaaaaa['account_name']
    r = requests.get(f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/receipts/v1/account/{acstid}/receipts",headers={"Content-Type": "application/json","Authorization": "bearer "+acstkn}) # dummy request
    try:
      if r.json()['errorCode'] == "errors.com.epicgames.common.authentication.token_verification_failed":
        print(f"[{Fore.MAGENTA}!{Fore.RESET}] Token is now invalid, restart the program. the autorefresher file auto refreshes your tokens as long as its open i would advise you run it.")
        input(f"[{Fore.MAGENTA}!{Fore.RESET}] Press ENTER to close...")
        shutil.rmtree(os.path.expandvars("%localappdata%")+"/FortniteAIO")
        exit()
    except Exception as e:
      print(e)
      input()
      pass
  os.system("clear || cls")
  print(mural)
  try:
    print(f"\n[{Fore.MAGENTA}!{Fore.RESET}] {authreq.json()['error_description']}. Please restart the software and enter a new code.")
    input("Press ENTER to exit the program...")
  except:
    while True:
      os.system("clear || cls")
      print(mural)
      print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Welcome {Fore.MAGENTA}{acstnm}{Fore.RESET}")
      ctypes.windll.kernel32.SetConsoleTitleW(f"FortniteAIO v{version} | Logged in as: {acstnm}")
      print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Please Select An Option:")
      print(f"[{Fore.MAGENTA}1{Fore.RESET}] Fortnite Battle Royale")
      print(f"[{Fore.MAGENTA}2{Fore.RESET}] Fortnite Save The World")
      print(f"[{Fore.MAGENTA}3{Fore.RESET}] Epic Games Account")
      print(f"[{Fore.MAGENTA}4{Fore.RESET}] Logout")
      opt = input(f"\n[{Fore.MAGENTA}?{Fore.RESET}] ")
      if opt == "1":
        os.system("clear || cls")
        print(mural)
        print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Current module : Fornite Battle Royale")
        print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Please Select An Option:")
        print(f"[{Fore.MAGENTA}1{Fore.RESET}] Get all skins")
        print(f"[{Fore.MAGENTA}2{Fore.RESET}] Turn Gifts On/Off")
        print(f"[{Fore.MAGENTA}3{Fore.RESET}] Back")
        opt = input(f"\n[{Fore.MAGENTA}?{Fore.RESET}] ")
        if opt == "1":
          headers={
            "Content-Type": "application/json",
            "Authorization": "bearer "+acstkn
          }
          skinsreq = requests.post(f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{acstid}/client/QueryProfile?profileId=athena",headers=headers,data="{}")
          items = skinsreq.json()['profileChanges'][0]['profile']['items']
          lily = []
          os.system("clear || cls")
          print(mural)
          print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Getting all skins please wait...")
          for skin in items:
            try:
              if 'cid' in skinsreq.json()['profileChanges'][0]['profile']['items'][skin]['templateId']:
                os.system("clear || cls")
                print(mural)
                print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Getting all skins please wait...")
                print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Currently got {len(lily)} (may have duplicates so skins may appear to be more than you actually have)")
                lily.append(skinsreq.json()['profileChanges'][0]['profile']['items'][skin]['templateId'])
              elif 'cid' in skinsreq.json()['profileChanges'][0]['profile']['items'][skin]['attributes']['cosmetic_item']:
                os.system("clear || cls")
                print(mural)
                print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Getting all skins please wait...")
                print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Currently got {len(lily)} (may have duplicates so skins may appear to be more than you actually have)")
                lily.append(skinsreq.json()['profileChanges'][0]['profile']['items'][skin]['attributes']['cosmetic_item'])
            except:
              pass
          print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Writing file, please wait...")
          skinsfull = ""
          lily = list(dict.fromkeys(lily))
          for item in lily:
            skin = requests.get(f"https://benbot.app/api/v1/cosmetics/br/search/ids?id={item.replace('AthenaCharacter:','')}&lang=en")
            skinsfull+=skin.json()[0]['name']+"\n"
          open(str(__file__).replace(os.path.basename(__file__),"skins.txt"),"w").write(f"""{len(lily)} SKINS

{skinsfull}""")
      
          
          input(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Done! press ENTER to go back...")
        elif opt == "2":
          os.system("clear || cls")
          print(mural)
          print(f"[{Fore.MAGENTA}1{Fore.RESET}] On")
          print(f"[{Fore.MAGENTA}2{Fore.RESET}] Off")
          print(f"[{Fore.MAGENTA}3{Fore.RESET}] Back")
          headers={
            "Content-Type": "application/json",
            "Authorization": "bearer "+acstkn
          }
          opt = input(f"\n[{Fore.MAGENTA}?{Fore.RESET}] ")
          if opt == "1":
            data = {"bReceiveGifts":True}
          elif opt == "2":
            data = {"bReceiveGifts":False}
          if opt == "1" or opt == "2":
            r = requests.post(f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{acstid}/client/SetReceiveGiftsEnabled?profileId=common_core",data=data,headers=headers)
            input(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Done! press ENTER to go back...")
      elif opt == "2":
        os.system("clear || cls")
        print(mural)
        print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Current module : Save The World")
        print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Please Select An Option:")
        print(f"[{Fore.MAGENTA}1{Fore.RESET}] Claim daily login reward.")
        opt = input(f"\n[{Fore.MAGENTA}?{Fore.RESET}] ")
        if opt == "1":#
          h = {
          "Content-Type": "application/json",
          "Authorization": "bearer "+acstkn
          }
          r = requests.post(f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{acstid}/client/ClaimLoginReward?profileId=campaign",data="{}",headers=h)
          try:
            r.json()['errorCode']
            input(f"\n[{Fore.MAGENTA}!{Fore.RESET}] ERROR ({r.json()}) \npress ENTER to go back...")
          except:
            print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] currently doesnt display the item claimed, will fix in future.")
            input(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Done! press ENTER to go back...")
      elif opt == "3":
        # EPIC
        os.system("clear || cls")
        print(mural)
        print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Current module : Epic Games")
        print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Please Select An Option:")
        print(f"[{Fore.MAGENTA}1{Fore.RESET}] Get all friends")
        print(f"[{Fore.MAGENTA}2{Fore.RESET}] Set support-a-creator code")
        print(f"[{Fore.MAGENTA}3{Fore.RESET}] Get all receipts")
        print(f"[{Fore.MAGENTA}4{Fore.RESET}] Back")
        opt = input(f"\n[{Fore.MAGENTA}?{Fore.RESET}] ")
        if opt == "1":
          # GET FRIENDS
          os.system("clear || cls")
          print(mural)
          headers={
            "Content-Type": "application/json",
            "Authorization": "bearer "+acstkn
          }
          r = requests.get(f"https://friends-public-service-prod.ol.epicgames.com/friends/api/v1/{acstid}/summary?displayNames=true",headers=headers)
          print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Writing file, please wait...")
          ben = ""
          for friend in r.json()['friends']:
            try:
              ben+=str(friend['displayName'])+"\n"
            except:
              pass
          ben = ben.encode("utf8")
          open(str(__file__).replace(os.path.basename(__file__),"friends.txt"),"wb").write(ben)
          input(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Done! press ENTER to go back...")
        elif opt == "2":
          os.system("clear || cls")
          print(mural)
          code = input(f"\n[{Fore.MAGENTA}?{Fore.RESET}] Please enter a creator code to support : ")
          headers={
            "Content-Type": "application/json",
            "Authorization": "bearer "+acstkn
          }
          data={
            "affiliateName": code
          }
          r = requests.post(f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{acstid}/client/SetAffiliateName?profileId=common_core",headers=headers,json=data)
          if "errorCode" in str(r.content):
            print(f"\n[{Fore.MAGENTA}!{Fore.RESET}] Invalid Creator Code")
            input(f"\n[{Fore.MAGENTA}+{Fore.RESET}] press ENTER to go back...")
          else:
            print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Set creator code to {code}")
            input(f"\n[{Fore.MAGENTA}+{Fore.RESET}] press ENTER to go back...")
        elif opt == "3":
          os.system("clear || cls")
          print(mural)
          print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Getting all receipts please wait...")
          headers={
            "Content-Type": "application/json",
            "Authorization": "bearer "+acstkn
          }
          r = requests.get(f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/receipts/v1/account/{acstid}/receipts",headers=headers)
          cntr = 0
          data = ""
          print(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Writing file, please wait...")
          for receipt in r.json():
            print(r.json())
            cntr += 1 
            data += f"""---- [ {cntr} ] ----
Platform purchased : {receipt['appStore']}
receipt id : {receipt['receiptId']}\n"""
          open(str(__file__).replace(os.path.basename(__file__),"receipts.txt"),"w").write(data)
          input(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Done! press ENTER to go back...")
      elif opt == "4":
        shutil.rmtree(os.path.expandvars("%localappdata%")+"/FortniteAIO")
        print(f"[{Fore.MAGENTA}+{Fore.RESET}] Removed the account. Closing in 1 second.")
        time.sleep(1)
        exit()

if __name__ == "__main__":
  main()
