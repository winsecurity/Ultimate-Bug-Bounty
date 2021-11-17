
import string


numbers = [0,1,2,3,4,5,6,7,8,9]

lowercase = string.printable[10:36]

uppercase = string.printable[36:62]

special = string.printable[62:92]


fd = open('rockyou-50.txt','r')
words = fd.read()
fd.close()


passwords = list(words.split('\n'))

#print(passwords)
# atleast one uppercase and one special and one number

numbers_yes = False
uppercase_yes = False
special_yes = False

for i in passwords:
	if len(i)>=8 and len(i)<=15:
		for j in numbers:
			if str(j) in i:
				numbers_yes = True
				break

		for j in uppercase:
			if j in i:
				uppercase_yes= True
				break

		for j in special:
			if j in i:
				special_yes= True
				break

		if (numbers_yes==True and uppercase_yes==True) or special_yes==True:
			print(i)

	numbers_yes = False
	uppercase_yes = False
	special_yes = False

