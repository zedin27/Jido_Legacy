'''
Little project to help and maintain my grandfather's legacy in journalism.
I will leave few resource links that I had to go through in my testing:
	Old project like Ford_hackathon for pip and virtual environment
	Python documentation for urllib library
	
'''

from click_link_content import link_content, html_content
import urllib.parse

#NOTE: How can I make a safe global variable for my URL to avoid any injection?

def page_number(pg_number=None):
	'''Return the current page number'''
	return

def paragraphs():
	'''
	Return the paragraph list of the specified URL
	NOTE: this is to test out. Step by step
	'''
	
	content = html_content("https://alrai.com/article/10796676/%D9%83%D8%AA%D8%A7%D8%A8/%D9%84%D9%8A%D8%B3-%D9%87%D9%86%D8%A7%D9%83-%D9%85%D8%B4%D9%83%D9%84%D8%A9-%D9%81%D9%84%D8%B3%D8%B7%D9%8A%D9%86%D9%8A%D8%A9")
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
	content = html_content("https://alrai.com/author/19/%D8%AF-%D8%B2%D9%8A%D8%AF-%D8%AD%D9%85%D8%B2%D8%A9")
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
				if not link.startswith('http'):
					link = urllib.parse.urljoin("https://alrai.com", link)
				titles_links.append((title, link))
			else:
				print("End tag not found")
		else:
			print("Title element was not found")

	for i, (title_name, link) in enumerate(titles_links):
		print(f"Title w/ URL {i+1}: {title_name} ({link})")
		link_content(link)
		# content_paragraphs(link)
	

print(content_paragraphs())
# jiddo_legacy()
# title()