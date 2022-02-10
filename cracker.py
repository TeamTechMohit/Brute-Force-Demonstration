import hashlib
from urllib.request import urlopen
 
def readwordlist(url):
    try:
        wordlistfile = urlopen(url).read()
    except Exception as e:
        print("Hey there was some error while reading the wordlist, error : ", e)
        exit()
    return wordlistfile
 
def hash(wordlistpassword):
    result = hashlib.sha1(wordlistpassword.encode())
    return result.hexdigest()
 
def bruteforce(guesspasswordlist, actual_password_hash):
	count=0
	for guess_password in guesspasswordlist:
		count=count+1
		if hash(guess_password) == actual_password_hash:
			print("Hey! your password is : ", guess_password,
                  "\n Please change this, it was really easy to guess it.")
	            # If the password is found then it will terminate the script here
			quit()
		elif hash(guess_password) != actual_password_hash:
			print(count," Password guess : ",str(guess_password)," does not match, trying next...")


actual_password = input('Enter your password which you want to compare in Brute force attack :: ')
actual_password_hash = hash(actual_password)
print('Your actual password hash is :: ',actual_password_hash)

url = input('Enter wordlist file link full of password guesses :: ')
wordlist = readwordlist(url).decode('UTF-8')
guesspasswordlist = wordlist.split('\n')
 
# Running the Brute Force attack
bruteforce(guesspasswordlist, actual_password_hash)
 
# It would be executed if your password was not there in the wordlist
print("Hey! I couldn't guess this password, it was not in my wordlist.")
 
 

#https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt

