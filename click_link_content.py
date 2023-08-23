'''Aux functions'''

# from urllib.request import urlopen
import requests

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def link_content(link):
	try:
		response = requests.get(link, headers=headers)
		response.raise_for_status()
		print("Visited link: ", link)
	except requests.exceptions.RequestException as e:
		print("Error visiting link: ", link)
		print(e)