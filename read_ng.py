# read.ng
# python 2.7

"""
book tracking app
 - title
 - author
 - start date
 - end date
"""

import cPickle as pickle
import os


class book(object):
	def __init__(self, title, author, startDate=""):
		self.title = title
		self.author = author
		self.startDate = startDate
		self.endDate = "..."

	def __str__(self):
		return self.title + " - " + self.author + " (" + self.startDate + " to " + self.endDate + ")"

print "=" * 45
print "=" * 45
print "Welcome to the book tracker"

if os.path.isfile("my_books.pkl"):
	try:
		pkl_in = open('my_books.pkl', 'rb')
		bookList = pickle.load(pkl_in) 
		pkl_in.close()
	except OSError:
		print "Problem loading from file"
else:
	bookList = []

user_input = ""

while user_input != 'e':
	print "-" * 55
	print 'n to add, l to list, f to finish, d to delete, e to exit, c to cancel'
	user_input = raw_input(":")
	if user_input == "n":
		user_input = raw_input("Add a book to the list?")
		if user_input != "c":
			title = raw_input("TITLE:")
			author = raw_input("AUTHOR:")
			startDate = raw_input("START DATE:")
			newBook = book(title, author, startDate)
			bookList.append(newBook)
			title, "-", author, "started on", startDate, "added to bookList."
	if user_input == 'd':
		user_input = raw_input("TITLE TO DELETE:")
		if user_input == "c":
			pass
		else:
			if user_input in [x.title for x in bookList]:
				bookPos = [x.title for x in bookList].index(user_input)
				user_input = raw_input("AUTHOR FOR CONFIRMATION:")
				if bookList[bookPos].author == user_input:
					print bookList[bookPos].title, "-", bookList[bookPos].author, "deleted from bookList."
					del bookList[bookPos]
				else:
					print "Deletion Cancelled."
	if user_input == 'f':
		title = raw_input("TITLE:")
		for listed_book in bookList:
			if listed_book.title == title:
				listed_book.endDate = raw_input("END DATE:")
	if user_input == 'l':
		if bookList:
			for listed_book in bookList:
				print listed_book
		else:
			print "No books listed"
	if user_input == 'e':
		pkl_out = open('my_books.pkl', 'wb')
		pickle.dump(bookList, pkl_out)
		pkl_out.close()	
		exit
		
