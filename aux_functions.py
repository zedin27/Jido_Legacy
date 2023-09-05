'''
Aux functions
'''

from urllib.request import urlopen
from requests.utils import requote_uri
import re

def html_content(url):
	'''Returns the DOCTYPE HTML as a big string'''
	response_page = urlopen(requote_uri(url))
	html_bytes = response_page.read()
	html_content = html_bytes.decode("utf-8")
	return html_content

def extract_paragraphs_text(text, start_tag=None, end_tag=None):
	'''Returns extracted content of a non-readable paragraph tag'''
	paragraphs = []
	
	for data in text.split('<br>'):
		paragraph = remove_html_tags(data).strip()
		if paragraph:
			paragraphs.append(paragraph)
	return paragraphs

def extract_paragraphs_p(text, start_tag, end_tag):
	'''Returns extracted content of a readable paragraph tag'''
	paragraphs = []
	start_index = 0

	while True:
		paragraph_start = text.find(start_tag, start_index)
		if paragraph_start == -1:
			break

		paragraph_end = text.find(end_tag, paragraph_start)
		if paragraph_end == -1:
			break

		paragraph = text[paragraph_start + len(start_tag):paragraph_end].strip()
		if paragraph:
			paragraphs.append(paragraph)

		start_index = paragraph_end + len(end_tag)
	return paragraphs

def remove_html_tags(text):
	'''Returns a cleaner content without tags (only used for non-paragraph tags)'''
	clean = re.compile('<.*?>')
	return re.sub(clean, '', text)

def title_chunk_generator(titles_links):
	'''Generates a state of the page number'''
	for i in range(0, len(titles_links), 10):
		yield titles_links[i:i + 10]