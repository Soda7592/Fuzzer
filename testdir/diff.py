import difflib
from pprint import pprint
html1 = open('response.html').readlines()
html2 = open('response2.html').readlines()

print(type(html1))

str_html1 = ''.join(str(element).strip('\n') for element in html1)
str_html2 = ''.join(str(element).strip('\n') for element in html2)


test = '123456789'
test2 = "12345@@@789"
d = difflib.Differ()
pprint(list(d.compare(test,test2)))