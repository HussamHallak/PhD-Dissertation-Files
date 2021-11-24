#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from boilerpy3 import extractors
from google_trans_new import google_translator
from collections import Counter
import stanza
import feedparser
import sys

stanza.download('en')

nlp = stanza.Pipeline(lang='en' , processors='tokenize,ner')

translator = google_translator()
extractor = extractors.ArticleExtractor()

TRACKED_CLASSES = ["GPE", "PERSON", "ORG", 'NORP']

def extract(url):

	try:
		content = extractor.get_content_from_url(url)
	except:
		print("This URL did not return a status code of 200. Try a different URL.")
		return
		
	content = content [0:3000]

	output = translator.translate(content)

	translated_content = output

	doc = nlp(translated_content)
	
	nes = []
	
	for item in doc.entities:
		nes.append((item.text, item.type))
			
	dedup_tags = Counter(nes)

	res = {k: [] for k in TRACKED_CLASSES}
	for item, count in dedup_tags.items():
		if item[1] in TRACKED_CLASSES:
			res[item[1]].append((item[0], count))
	return res

def extract_data_from_rss(url):
	d = feedparser.parse(url)
	return d.entries


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print ("Usage: Python3 extract_NE.py <url>")
		print ("e.g: python3 extract_NE.py http://example.com")
		sys.exit()
	else:
		url = sys.argv[1]
		posts = extract_data_from_rss(url)
		for post in posts:
			print ('Entities from post:', post.link, post.title)
			ext_entities = extract(post.link)
			if not ext_entities:
				sys.exit()
			entities_count = 0
			for cat in TRACKED_CLASSES:
				print("----------- " + cat + " -------------")
				for e in ext_entities[cat]:
					print(e[0], e[1])
					entities_count+=e[1]
			print ('entities count = ', entities_count)
			print('=======================================================================')
