'''
Little project to help and maintain my grandfather's legacy in journalism.
I will leave few resource links that I had to go through in my testing:
	Old project like Ford_hackathon for pip and virtual environment
	Python documentation for urllib library
	
'''

from click_link_content import link_content, html_content
import urllib.parse
import time
import re
import html

#NOTE: How can I make a safe global variable for my URL to avoid any injection?

def pgno(url):
	'''Return the current page number'''
	separator = '?' if '?' not in url else '&'
	pattern = r'(pgno=\d+)'
	new_pg_number = 2
	replace = f'pgno={new_pg_number}'

	if re.search(pattern, url):
		new_url = re.sub(pattern, replace, url)
	else:
		new_url = f'{url}{separator}{replace}'
	return new_url

def paragraphs(url):
	'''
	Return the paragraph list of the specified URL
	NOTE: this is to test out. Step by step
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
				# paragraph = html.unescape(paragraph)
				# print(paragraph)
				paragraphs.append(paragraph)
				paragraph_start = paragraph_end + len('</p>')
			else:
				print("Closing </p> tag not found")
				break
	else:
		print("Paragraph element was not found")

	return paragraphs

def jiddo_legacy():
	'''
	Idea is to have each article title stored in an index with the text in it
	(e.g. article[0] would have the title name and the content of the paragraph, article[1] next title, article[n + 1] for the rest)
	'''

	url = "https://alrai.com/author/19/%D8%AF-%D8%B2%D9%8A%D8%AF-%D8%AD%D9%85%D8%B2%D8%A9?pgno=1" #NOTE: I need to test how to parse non-ASCII characters
	content = html_content("https://alrai.com/author/19/%D8%AF-%D8%B2%D9%8A%D8%AF-%D8%AD%D9%85%D8%B2%D8%A9")
	titles_links = []
	target_element_title_article = '<div class="title-article">'
	start_index = 0
	flag_processing = True
	
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
				if not link.startswith('http'):
					link = urllib.parse.urljoin("https://alrai.com", link)
				titles_links.append((title, link))
			else:
				print("End tag not found")
		else:
			flag_processing = False

	for i, (title_name, link) in enumerate(titles_links):
		print(f"Title w/ URL {i+1}: {title_name} ({link})")
		print("Paragraphs:")
		paragraph_list = paragraphs(link)
		for j, paragraph in enumerate(paragraph_list):
			print(f"Paragraph {j + 1}: {paragraph}")
		print("I O " * 42)
	
	next_page_url = pgno(url)
	print("Next page: ", next_page_url)

jiddo_legacy()