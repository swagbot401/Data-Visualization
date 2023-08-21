import random, sys, time
import webbrowser as web
import requests, bs4


# web.open('https://inventwithpython.com/')
# web.open('https://tesla.com')

# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# print(res)

#Checking if request succeeded 
#(Full List of codes: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
# if (res.status_code == requests.codes.ok):
#     print("It workss")
# else: 
#     print("Something is wrong!")


# print(len(res.text))
# print(res.text[:250])


# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# res.raise_for_status()

# exampleFile = open('example.html')
# exampleSoup = bs4.be

# res = requests.get('https://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(noStarchSoup))

# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')

# elems = exampleSoup.select('#author')
# print(str(elems[0]))
# print("-------------")
# print(elems[0].get_text())
# print("------------")
# print(elems[0].attrs)

soup = bs4.BeautifulSoup(open("example.html"), "html.parser")
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('some_nond') == None)


