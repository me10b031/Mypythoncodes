'''Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the user name of a given email address.
Both user names and company names are composed of letters only.'''


'''import re
emailAddress = input()
user = "(\w+)@(\w+\.)(com)"
username = re.match(user,emailAddress)
print (username.group(2))'''

import re
emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print (r2.group(2))
