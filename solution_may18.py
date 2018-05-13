#! /usr/bin/python3


#listing the only possible characters in the deciphered message
from string import ascii_letters
import re
from webscraper import WebpageScraper

valid_characters = ascii_letters + " .,@:" + "0123456789"

#reading the cypher after scraping the quiz webpage
scraper = WebpageScraper()
QUIZ_URL = "https://www.gambitresearch.com/quiz/"
quiz_page = scraper(QUIZ_URL)

#reading the ciphered message from the page body content
page_content = str(quiz_page.body)
cipher = re.findall("\d+", page_content)
cipher = list(map( int, cipher))

#3 cypher shifts for 3 possible offsets
offsets = list(range(3))
offset2shift = {}

#for each offset we group the letter and attempt every possible shift (<256) until finding one giving only acceptable characters
for offset in offsets:
	message = cipher[offset::3] #doing it for a single shift

	for shift in range(256):
		for letter in message:
			#applying shift
			letter = chr( (letter - shift) % 256)
			#if letter not in acceptable characters rejecting shift value
			if letter not in valid_characters:
				break
		else:
			#shift has not been rejected, here it must be the right one
			offset2shift[ offset] = shift
			break

#printing the deciphered message
for index, letter in enumerate( cipher):
	letter = chr( (letter - offset2shift[index%3]) % 256)
	print( letter, end="")
print()
