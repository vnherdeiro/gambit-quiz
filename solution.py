#! /usr/bin/python3


#listing the only possible characters in the deciphered message
from string import ascii_letters
valid_characters = ascii_letters + " .,@:" + "0123456789"

cipher = [183,12,2,219,22,194,143,234,5,221,14,8,208,27,11,219,8,10,216,22,4,226,199,252,222,25,
	182,226,22,2,229,16,4,214,199,10,215,12,182,182,8,3,209,16,10,143,10,254,208,19,2,212,21,253,212,
	213,182,191,19,251,208,26,251,143,26,251,221,11,182,232,22,11,225,199,9,222,19,11,227,16,5,221,199,
	247,221,11,182,178,253,182,227,22,182,216,10,247,221,10,5,211,12,214,214,8,3,209,16,10,225,12,9,212,
	8,8,210,15,196,210,22,3,143,24,11,222,27,255,221,14,182,225,12,252,212,25,251,221,10,251,169,199,252,
	162,224,207,165,223,206,165,215,250,157]

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
