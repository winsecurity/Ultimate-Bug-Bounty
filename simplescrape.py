
import requests


url = "http://206.189.124.249:31468/forgot.php"

#userid=htbadmin&submit=submit
data = {
	"userid":"htbadmin",
	"submit":"submit"
}

r = requests.post(url,data=data)

print(r.text)
