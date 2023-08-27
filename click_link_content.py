'''Aux functions

RESOURCES:
	https://stackoverflow.com/questions/489999/convert-list-of-ints-to-one-number
	Encoding problem: https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
	URI encode: https://stackoverflow.com/a/54135995/6017248

'''

from urllib.request import urlopen
from requests.utils import requote_uri
from urllib.error import HTTPError, URLError

def html_content(url):
	response_page = urlopen(url)
	html_bytes = response_page.read()
	html_content = html_bytes.decode("utf-8")
	return html_content

def link_content(link):
	try:
		response = urlopen(requote_uri(link))
		current_url = response.read().decode("utf-8")
		print("current_url: ", current_url)
	except HTTPError as e:
		print("HTTP Error visiting link: ", link)
		print(e)
	except URLError as e:
		print("URL Error visiting link: ", link)
		print(e)
