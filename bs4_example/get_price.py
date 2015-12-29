#!/usr/bin/env python

import sys
import urllib2
from bs4 import BeautifulSoup


def print_result(soup):
	print("{0:12}, {1:9}, {2:12}, {3:9}".format(soup[0].string, soup[4].string, soup[5].string, soup[6].string))
	
if __name__ == "__main__":
	if len(sys.argv) == 2:
		stock = sys.argv[1]
	else:
		print("please input stock number")
		exti()
	
	# Quote for Jan, 3, 2011
	url_head = 'http://finance.yahoo.com/q/hp?s='
	url_end = '.TW&a=00&b=3&c=2011&d=00&e=3&f=2011&g=d'
	url_full = url_head + stock + url_end
	
	response = urllib2.urlopen(url_full)  
	html = response.read()
	soup = BeautifulSoup(html, 'lxml')
	table = soup.find('table', class_='yfnc_datamodoutline1')
	title = table.find_all('th', class_='yfnc_tablehead1')
	value = table.find_all('td', class_='yfnc_tabledata1')
	
	print_result(title)
	print_result(value)
	
	# Quote for Jan, 6, 2012
	url_head = 'http://finance.yahoo.com/q/hp?s='
	url_end = '.TW&a=00&b=6&c=2012&d=00&e=6&f=2012&g=d'
	url_full = url_head + stock + url_end
	
	response = urllib2.urlopen(url_full)  
	html = response.read()
	soup = BeautifulSoup(html, 'lxml')
	table = soup.find('table', class_='yfnc_datamodoutline1')

	value = table.find_all('td', class_='yfnc_tabledata1')
	
	print_result(value)
	
	
	# Quote for Jan, 2, 2013
	url_head = 'http://finance.yahoo.com/q/hp?s='
	url_end = '.TW&a=00&b=2&c=2013&d=00&e=2&f=2013&g=d'
	url_full = url_head + stock + url_end
	
	response = urllib2.urlopen(url_full)  
	html = response.read()
	soup = BeautifulSoup(html, 'lxml')
	table = soup.find('table', class_='yfnc_datamodoutline1')

	value = table.find_all('td', class_='yfnc_tabledata1')
	
	print_result(value)
	# Quote for Jan, 2, 2014
	url_head = 'http://finance.yahoo.com/q/hp?s='
	url_end = '.TW&a=00&b=2&c=2014&d=00&e=2&f=2014&g=d'
	url_full = url_head + stock + url_end
	
	response = urllib2.urlopen(url_full)  
	html = response.read()
	soup = BeautifulSoup(html, 'lxml')
	table = soup.find('table', class_='yfnc_datamodoutline1')

	value = table.find_all('td', class_='yfnc_tabledata1')
	
	print_result(value)
	# Quote for Jan, 5, 2015
	url_head = 'http://finance.yahoo.com/q/hp?s='
	url_end = '.TW&a=00&b=5&c=2015&d=00&e=5&f=2015&g=d'
	url_full = url_head + stock + url_end
	
	response = urllib2.urlopen(url_full)  
	html = response.read()
	soup = BeautifulSoup(html, 'lxml')
	table = soup.find('table', class_='yfnc_datamodoutline1')

	value = table.find_all('td', class_='yfnc_tabledata1')
	
	print_result(value)
	# Quote for Dec, 1, 2015
	url_head = 'http://finance.yahoo.com/q/hp?s='
	url_end = '.TW&a=11&b=1&c=2015&d=11&e=1&f=2015&g=d'
	url_full = url_head + stock + url_end
	
	response = urllib2.urlopen(url_full)  
	html = response.read()
	soup = BeautifulSoup(html, 'lxml')
	table = soup.find('table', class_='yfnc_datamodoutline1')

	value = table.find_all('td', class_='yfnc_tabledata1')
	
	print_result(value)
	
	
	
	
	
	
	