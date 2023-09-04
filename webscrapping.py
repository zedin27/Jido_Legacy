'''
Little project to help and maintain my grandfather's legacy in journalism.
I will leave few resource links that I had to go through in my testing:
	Old project like Ford_hackathon for pip3 and virtual environment (venv)
	Python documentation for urllib library
	Regex documentation w/ chatGPT to avoid hassle
	Joe lole: https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
		-->		cfscrape() suggestion
	Removing the pesky <font> and make it as a paragraph: https://stackoverflow.com/questions/77034768/web-scrape-multiple-paragraphs-in-an-arabic-website-that-has-p-and-font-html
	Time to finish program (as for 9/4/2023):
		python3 webscrapping.py  5.86s user 0.63s system 3% cpu 3:24.91 total
		python3 webscrapping.py  4.74s user 0.65s system 3% cpu 2:55.27 total (not working, so it is just not parsing the paragraphs)
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
	'''Return the paragraph list of the specified URL'''

	content = html_content(url)
	paragraphs = []
	start_tag = '<div class="item-article-body size-20">'
	end_tag = '</div>\n</div>\n</div>'
	start_index = content.find(start_tag)
	end_index = content.find(end_tag, start_index)

	if start_index != -1 and end_index != -1:
		extracted_text = content[start_index + len(start_tag):end_index]
		temp = extracted_text.split('<br>')
		for data in temp:
			paragraph = remove_html_tags(data).strip()
			if paragraph:
				paragraphs.append(paragraph)
		return paragraphs
	else:
		print("Article not found ")
		return []

def remove_html_tags(text):
	clean = re.compile('<.*?>')
	return re.sub(clean, '', text)

def title_chunk_generator(titles_links):
	for i in range(0, len(titles_links), 10):
		yield titles_links[i:i + 10]


def jiddo_legacy():
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
		print(f"Going to the next page number: {url}")

jiddo_legacy()