import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
bat
pat
sat
'''

sentence = 'Start a sentence and then bring it to an end'

#raw strings
print('\ttab')
print(r'\ttab')

#search pattern
pattern = re.compile(r'ABC') # case and order sensitive
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print(text_to_search[28:31])

#special character
pattern = re.compile(r'coreyms\.com') # . is a special character, look in snippets.txt
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

pattern = re.compile(r'^Star') # ^ is a special character, look in snippets.txt
matches = pattern.finditer(sentence)
for match in matches:
    print(match)

#phone number
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # 3 digits followed by character followed by three digits followed by character followed by four digits
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

#phone number from external file
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') 
with open('data.txt', 'r') as f:
    content = f.read()
    matches = pattern.finditer(content)
    for match in matches:
        print(match)

#matching specific characters
pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d') # specify inside of []
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d') # phone numbers starting with 800 and 900
with open('data.txt', 'r') as f:
    content = f.read()
    matches = pattern.finditer(content)
    for match in matches:
        print(match)

#specifying range
pattern = re.compile(r'[a-zA-Z]') # use hyphon - everything that is lowercase or uppercase a-z
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

#negation
pattern = re.compile(r'[^a-zA-Z]') # use caret - everything that is not lowercase or uppercase a-z
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

pattern = re.compile(r'[^b]at') # everything that ends with at and doesnt start with b
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

#quantifiers
pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # curly braces to specify repitition
with open('data.txt', 'r') as f:
    content = f.read()
    matches = pattern.finditer(content)
    for match in matches:
        print(match)

pattern = re.compile(r'Mr.?\s[A-Z]\w*') # period is made optional by ? and 0 or more words after capital using * for Mr. T
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

#groups
pattern = re.compile(r'M(r|s|rs).?\s[A-Z]\w*') # different groups seperated by | inside parantheses ()
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

#findall
pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # returns groups as strings in list
matches = pattern.findall(text_to_search)
for match in matches:
    print(match)

#match
pattern = re.compile(r'Start')
matches = pattern.match(sentence) # returns match of Start in sentence only in beginning of string
print(matches)

#search
pattern = re.compile(r'sentence')
matches = pattern.search(sentence) # returns first match of sentence in sentence across whole string
#returns None if no matches
print(matches)

#flags
pattern = re.compile(r'start', re.IGNORECASE) # flag for ignore case, shorthand is I
matches = pattern.search(sentence)
#returns None if no matches
print(matches)