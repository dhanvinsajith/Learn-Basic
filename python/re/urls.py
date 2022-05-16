import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)



urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# group 0 is everything captured, group 1 is www., group 2 is domain name, group 3 is top level domain

subbed_urls = pattern.sub(r'\2\3', urls) # prints groups 2 and 3
print(subbed_urls)

matches = pattern.finditer(urls)
for match in matches:
    print(match.group(0)) # prints group 0