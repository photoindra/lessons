# Программа, скачивающая данные с сайтов. Программа должна принимать на вход адрес страницы, анализировать её содержимое и сохранять отдельно в читаемом виде интересующие данные. Например, это могут быть новости с какого-то новостного сайта, либо записи из блога.


import urllib.request
import urllib.parse
import re

url = 'http://www.soundonsound.com/sos/jun04/articles/synthsecrets.htm'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

title = re.findall(r'<title>(.+?)</title>', str(respData))
paragraphs = re.findall(r'<\s*p[^>]*>([^<]*)<\s*\/\s*p\s*>', str(respData))

image = re.findall(r'img+\s+src="http://media.soundonsound.com/sos/([^<]+)"',str(respData))

saveFile = open('results.html', 'w')

saveFile.write('<h2>' + str(title[0]) + '</h2>')
for eachP in paragraphs:
    saveFile.write('<p>' +str(eachP) + '</p>')
newArticle = '<br>'
saveFile.write(newArticle)
saveFile.close()

