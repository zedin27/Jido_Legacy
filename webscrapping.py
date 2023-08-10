'''
Little project to help and maintain my grandfather's legacy journalism
'''
from urllib.request import urlopen

def jiddo_legacy():
	'''
	Idea is to have each article title stored in an index with the text in it (e.g. article[0] would have the title with the text)
	'''

	# url = "https://alrai.com/author/19/د-زيد-حمزة" #NOTE: I need to test how to parse non-ASCII characters
	url = "https://alrai.com/author/19/%D8%AF-%D8%B2%D9%8A%D8%AF-%D8%AD%D9%85%D8%B2%D8%A9"
	response_page = urlopen(url)
	html_bytes = response_page.read()
	html_content = html_bytes.decode("utf-8")
	page_number = 0 # After reading the articles, go to the next page number (should be after 10 or less) 
	
	target_element_title_article = '<div class="title-article">'
	start_index = html_content.find(target_element_title_article)
	if start_index != -1:
		start_index += len(target_element_title_article)
		end_index = html_content.find('</div>', start_index)
		print(end_index)

		if end_index != -1:
			content_title_article = html_content[start_index:end_index].strip()
			title_start = content_title_article.find('title="') + len('title="')
			title_end = content_title_article.find('">', title_start)
			title = content_title_article[title_start:title_end]
			print(title)
		else:
			print("Title not found")
	# return

jiddo_legacy()