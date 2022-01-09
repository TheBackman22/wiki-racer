# python program to build a data set / 
# (directional) adjacency_graph(.py) of [eventually all]
# wikipedia pages
# and a function to shortest path though it
# and a way to import a [somehow stored adjacency list]
# to shortest path over

import requests
# BeautifulSoup is imported with the name bas4 
from bs4 import BeautifulSoup as bs
# website navigating using https://www.kindacode.com/article/extract-all-links-from-a-webpage-using-python-and-beautiful-soup-4/
import sys #program args

import re

starting_page = ""
current_page = ""

def main():

	global starting_page, current_page
	starting_page = str(sys.argv[1])
	current_page = str(sys.argv[1])
	if len(sys.argv) != 2:
		print("incorrect args")
		exit(1)
	elif re.search(' +', starting_page): # if somehow theres a space in a single argument?
		print("Invalid starting page")
	
	print("Starting webpage: %s" % starting_page)
	get_all_wiki_links(starting_page)

# get a dictionary (?) of all available wikipedia page links on the current
# wiki page
# https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/
def get_all_wiki_links(current_page):
	start_url = starting_page
	print(start_url)
	res = requests.get(start_url)
	print(res.status_code)
	# if not res.raise_for_status():
	# 	print("connection to page unsuccessful")
	# 	exit(1)
	soup = bs(res.content, 'html.parser')
	every_link = soup.find(id="bodyContent").find_all('a')
	all_links = []
	i = 0
	for link in every_link:
		if link.get('href','').find("/wiki/") != -1 and link.get('title','') != "":
			all_links.append(link.get('title','').replace(' ', '_'))
	print(all_links.index("Staple_food"))

	return all_links



#from a starting page
def recursive_DataBuild():
	#build an adjacency list (defined in adjacency_list.py)
	# of all the links on a page for a set number of iterations 
	# (every link on every page on minimum 2 pages)
	return
	
main()
	