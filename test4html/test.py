import urllib
from urllib import request

import bs4

request
res = request.urlopen('https://www.aliyun.com/jiaocheng/435800.html').read()
res = res.decode('utf-8')
pagesoup = bs4.BeautifulSoup(res)
# print(pagesoup)
#select返回的结果是list
# print(pagesoup.select('a'))#所有名为<a>的元素
# print(pagesoup.select('#author'))#id属性为author的元素
#print(pagesoup.select('.product-title-tip'))#class属性为product-title-tip的元素
# print(pagesoup.select('div span'))#所有在<div>之内的<span>元素
# print(pagesoup.select('div > span'))#所有直接在<div>元素之内的<span>元素，中间没有其他元素
# print(pagesoup.select('a[data-spm-click]'))#<a>属性名为data-spm-click
# print(pagesoup.select('a[target="_blank"]'))#<a>属性名为target，且值等于_blank
elem = pagesoup.select('span[class="ali-main-time-what"]')
print(type(elem[0]))
print(elem[0].attrs)
print(type(str(elem[0])))
print(str(elem[0]))
print(type(elem[0]))
print(elem[0].attrs)