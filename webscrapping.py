'''
Little project to help and maintain my grandfather's legacy in journalism.
I will leave few resource links that I had to go through in my testing:
	Old project like Ford_hackathon for pip and virtual environment
	Python documentation for urllib library
'''

from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup
import lxml

#NOTE: How can I make a safe global variable for my URL to avoid any injection?

def page_number(pg_number=None):
	'''Return the current page number'''
	return

def html_content():
	url = "https://alrai.com/author/19/%D8%AF-%D8%B2%D9%8A%D8%AF-%D8%AD%D9%85%D8%B2%D8%A9"
	response_page = urlopen(url)
	html_bytes = response_page.read()
	html_content = html_bytes.decode("utf-8")
	return html_content

def title(arr=None, idx=None):
	'''Return index (idx) from the list of titles (arr)'''
	url = "https://alrai.com/author/19/%D8%AF-%D8%B2%D9%8A%D8%AF-%D8%AD%D9%85%D8%B2%D8%A9"
	content = html_content()
	soup = BeautifulSoup(content, 'html.parser')
	links = soup.find_all('a', class_='size-17 font-700')
	print(links)

	for link in links:
		link_url = link.get('href')
		if link_url:
			if not link_url.startswith('http'):
				link_url = urllib.parse.urljoin(url, link_url)
				
	return link_url

def paragraph(idx=None): #NOTE: maybe have this in the same title function?
	return

def find(content, target, target2, beginning, end):
	'''
	HTML content with two target values (one that starts with and other that ends), beginning and ending index for parsing
	Need to work more on this portion of the code if it becomes unreadable
	'''

	content = html_content()
	target = '<div class="title-article">'
	target2 = '</div>'
	beginning = 0
	titles_link = []

	while beginning != -1:
		beginning = content.find(target, beginning)

		if beginning != -1:
			beginning += len(target)
			end = content.find(target2, beginning)

			if end != -1:
				content_title_article = content[beginning:end].strip()
				title_start = content_title_article.find('title="') + len('title="')
				title_end = content_title_article.find('>"', title_start)
				title_name = content_title_article[title_start:title_end].replace('\r', '')
				titles_link.append(title_name)
			else:
				print("End tag not found")
		else:
			print("Title element was not found")
	return titles_link

def jiddo_legacy():
	'''
	Idea is to have each article title stored in an index with the text in it
	(e.g. article[0] would have the title name and the content of the paragraph, article[1] next title, article[n + 1] for the rest)
	'''

	# url = "https://alrai.com/author/19/د-زيد-حمزة" #NOTE: I need to test how to parse non-ASCII characters
	content = html_content()
	titles_links = []
	target_element_title_article = '<div class="title-article">'
	start_index = 0
	page_number = 0 # After reading the articles, go to the next page number (should be after 10 or less)
	
	while start_index != -1:
		start_index = content.find(target_element_title_article, start_index)
		
		if start_index != -1:
			start_index += len(target_element_title_article)
			end_index = content.find('</div>', start_index)

			if end_index != -1:
				content_title_article = content[start_index:end_index].strip()
				title_start = content_title_article.find('title="') + len('title="')
				title_end = content_title_article.find('">', title_start)
				title = content_title_article[title_start:title_end].replace('\r', '')

				link_start = content_title_article.find('href="') + len('href="')
				link_end = content_title_article.find('"', link_start)
				link = content_title_article[link_start:link_end].replace('\r', '')
				if not link.startswith('https'):
					link = urllib.parse.urljoin("https://alrai.com", link)
				titles_links.append((title, link))
				# titles_links.append(title)
			else:
				print("End tag not found")
		else:
			print("Title element was not found")

	for i, (title_name, link) in enumerate(titles_links):
		print(f"Title w/ URL {i+1}: {title_name} ({link})")

jiddo_legacy()
# title()