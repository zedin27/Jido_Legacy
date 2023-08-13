'''
Little project to help and maintain my grandfather's legacy in journalism
'''
from urllib.request import urlopen

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
	return

def paragraph(idx=None): #NOTE: maybe have this in the same title function?
	return

def jiddo_legacy():
	'''
	Idea is to have each article title stored in an index with the text in it
	(e.g. article[0] would have the title name and the content of the paragraph, article[1] next title, article[n + 1] for the rest)
	'''

	# url = "https://alrai.com/author/19/د-زيد-حمزة" #NOTE: I need to test how to parse non-ASCII characters
	content = html_content()
	titles = []
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
				title = content_title_article[title_start:title_end]
				title = title.replace('\r', '').strip()
				titles.append(title)
			else:
				print("End tag not found")
		else:
			print("Title element was not found")

	for i, title_name in enumerate(titles): #NOTE: some titles just doesn't print at all (e.g. title 4)
		print(f"Title {i+1}: {title_name}")
	print(titles)

jiddo_legacy()