# '''Aux functions'''

# # from urllib.request import urlopen
# import requests

# headers = {
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }

# def link_content(link):
# 	try:
# 		response = requests.get(link, headers=headers)
# 		print("Visited link: ", link, "\n")
# 	except requests.exceptions.RequestException as e:
# 		print("Error visiting link: ", link)
# 		print(e)

'''Aux functions

RESOURCES:
	https://stackoverflow.com/questions/489999/convert-list-of-ints-to-one-number
	Encoding problem: https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
	URI encode: https://stackoverflow.com/a/54135995/6017248

'''



import re
import urllib.request
import urllib.parse
from requests.utils import requote_uri
from urllib.error import *

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def link_content(link):
	print("Given link: ", link)
	regexd = r"/\d+/.+"
	match = re.search(regexd, link)
	matched = match.group()
	try:
		# newurl = 'https://www.alrai.com/article' + matched
		# print(requote_uri(newurl))
		# print("newurl: ", url_encode)
		response = urllib.request.urlopen(requote_uri(link))
		print("Visited link: ", link, "\n")
		print(response)
	except HTTPError as e:
		print("HTTP Error visiting link: ", link)
		print(e)
	except URLError as e:
		print("URL Error visiting link: ", link)
		print(e)
	

# link = "https://alrai.com/article/10785313/%D9%83%D8%AA%D8%A7%D8%A8/%D9%85%D8%B5%D8%B7%D9%84%D8%AD%D8%A7%D8%AA-%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF%D9%8A%D8%A9-%D8%AA%D8%A8%D8%AF%D9%84%D8%AA-%D9%85%D8%B9%D8%A7%D9%86%D9%8A%D9%87%D8%A7"
# link_content
