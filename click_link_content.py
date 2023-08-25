'''Aux functions

RESOURCES:
	https://stackoverflow.com/questions/489999/convert-list-of-ints-to-one-number
	Encoding problem: https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
	URI encode: https://stackoverflow.com/a/54135995/6017248

'''

import urllib.request
from requests.utils import requote_uri
from urllib.error import HTTPError, URLError

def link_content(link):
	try:
		response = urllib.request.urlopen(requote_uri(link))
		print("Visited link: ", response, "\n")
	except HTTPError as e:
		print("HTTP Error visiting link: ", link)
		print(e)
	except URLError as e:
		print("URL Error visiting link: ", link)
		print(e)
