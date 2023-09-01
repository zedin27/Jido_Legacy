'''
Little project to help and maintain my grandfather's legacy in journalism.
I will leave few resource links that I had to go through in my testing:
	Old project like Ford_hackathon for pip3 and virtual environment (venv)
	Python documentation for urllib library
	Regex documentation w/ chatGPT to avoid hassle
	
'''

from click_link_content import html_content
import urllib.parse
import re

#NOTE: How can I make a safe global variable for my URL to avoid any injection?
increment = 1
def pgno(url):
	'''Return the current page number'''
	
	global increment
	separator = '?' if '?' not in url else '&'
	pattern = r'(pgno=\d+)'
	replace = f'pgno={increment}'

	if re.search(pattern, url):
		new_url = re.sub(pattern, replace, url)
		increment += 1
	else:
		new_url = f'{url}{separator}{replace}'
	return new_url

def paragraphs(url):
	'''
	Return the paragraph list of the specified URL
	NOTE: this is to test out. Step by step. Need it to work for paragraphs
			that has <font> on it, and doesn't break in the parse
			flags for <font> and <p>?
	'''

	content = html_content(url)
	paragraphs = []
	target_element_paragraph_article = '<div class="item-article-body size-20">'
	start_index = content.find(target_element_paragraph_article)

	if start_index != -1:
		start_index += len(target_element_paragraph_article)
		content_paragraph = content[start_index:].strip()
		paragraph_start = content_paragraph.find('<p>')

		while paragraph_start != -1:
			paragraph_end = content_paragraph.find('</p>', paragraph_start)

			if paragraph_end != -1:
				paragraph = content_paragraph[paragraph_start + len('<p>'):paragraph_end].strip()
				paragraphs.append(paragraph)
				paragraph_start = paragraph_end + len('</p>')
			else:
				print("Closing </p> tag not found")
				break
	else:
		print("Paragraph element was not found")

	return paragraphs

def title_chunk_generator(titles_links):
	for i in range(0, len(titles_links), 10):
		yield titles_links[i:i + 10]


def jiddo_legacy():
	'''
	Idea is to have each article title stored in an index with the text in it
	(e.g. article[0] would have the title name and the content of the paragraph, article[1] next title, article[n + 1] for the rest)
	'''

	url = "https://alrai.com/author/19/د-زيد-حمزة?pgno=1"
	title_hashmap = {}

	while True:
		starting_content = html_content("https://alrai.com/author/19/د-زيد-حمزة")
		titles_links = []
		target_element_title_article = '<div class="title-article">'
		start_index = 0
		starting_content = html_content(url)

		while start_index != -1:
			start_index = starting_content.find(target_element_title_article, start_index)
			
			if start_index != -1:
				start_index += len(target_element_title_article)
				end_index = starting_content.find('</div>', start_index)

				if end_index != -1:
					content_title_article = starting_content[start_index:end_index].strip()
					title_start = content_title_article.find('title="') + len('title="')
					title_end = content_title_article.find('">', title_start)
					title = content_title_article[title_start:title_end].replace('\r', '')

					link_start = content_title_article.find('href="') + len('href="')
					link_end = content_title_article.find('"', link_start)
					link = content_title_article[link_start:link_end].replace('\r', '')
					if not link.startswith('http'):
						link = urllib.parse.urljoin("https://alrai.com", link)
					titles_links.append((title, link))
				else:
					print("End tag not found")
			else:
				starting_content = pgno(url)
		if not titles_links:
			print("No more titles")
			break

		chunk_generator = title_chunk_generator(titles_links)
		for title_chunk in chunk_generator:
			for i, (title_name, link) in enumerate(title_chunk):
				if title_name in title_hashmap:
					print(f"Skipping title: {title_name}")
					continue
				title_hashmap[title_name] = link
				print(f"Title w/ URL {i+1}: {title_name} ({link})")
				paragraph_list = paragraphs(link)
				for j, paragraph in enumerate(paragraph_list):
					print(f"Paragraph {j + 1}: {paragraph}")
				print("I O " * 42)
		url = pgno(url)

jiddo_legacy()