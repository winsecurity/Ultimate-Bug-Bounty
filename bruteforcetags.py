
import requests


fd = open('tags.txt','r')
tags = fd.read()
fd.close()


tags = list(tags.split('\n'))

fd = open('attributes.txt','r')
attrs = fd.read()
fd.close()


attrs = list(attrs.split('\n'))


url = "https://ac721ff91ea5e674c03a08a600200053.web-security-academy.net/?search="


for i in tags:
	new_url = url + "<{}>".format(i) 

	r = requests.get(new_url)
	if r.status_code ==200:
		print(i)
