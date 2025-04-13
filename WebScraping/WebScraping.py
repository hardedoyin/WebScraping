# import the requests HTTP library and BeautifulSoup for parsing HTML
from turtle import title
import requests
from bs4 import BeautifulSoup
import pprint

# make a GET request to the Hacker News homepage
res = requests.get('https://news.ycombinator.com/')
# check if the request was successful (status code 200)
#print(res)
# if the request was successful, parse the HTML content using BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())
# select all elements with the class 'score' (which contains the points for each post)
subtext = (soup.select('.subtext'))
links = (soup.select('.titleline > a'))

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtext):
	# create a list to store the custom Hacker News posts
	custom_hn = []
	# iterate through each element in the subtext list
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.getText('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
		# check if the points are greater than or equal to 100
		if points > 99:
		# create a dictionary with the title and link of the post
			custom_hn.append({'title': title, 'link': href, 'votes': points})
	return sort_stories_by_votes(custom_hn)
pprint.pprint(create_custom_hn(links, subtext))

