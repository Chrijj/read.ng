# read.ng - 0.6
# python 2.7

"""
book tracking app
 - title
 - author
 - start date
 - end date
"""

import cPickle as pickle
import datetime as dt 
import os

class bookList(object):
	"""collection of book objects"""
	def __init__(self, name):
		self.name = name
		self.bookCount = 0
		self.books = {}

	def addBook(self, book):
		self.books[self.bookCount] = book
		book.title, "-", book.author, "started on", book.startDate, "added to bookList."
		self.bookCount += 1

	def listBooks(self):
		if self.books:
			for eachBook in self.books.values():
				print str(eachBook)
		else:
			print "No books exist in list %s" % self.name

	def addSession(self, sessionDate, paegUpTo):
		self.books[self.bookCount-1].finishedSession(sessionDate, pageUpTo)
		print str(self.books[self.bookCount-1])
		print "Currently up to page %s out of %s pages." % (self.books[self.bookCount-1].currentPage, self.books[self.bookCount-1].pageCount)

	def finishBook(self, title):
		for count, book in self.books.items():
			if book.title == title:
				user_input = raw_input("Did you finish the book today? (y/n)?")
				if user_input == 'y':
					finishDate = dt.date.today()
				else:
					year = int(raw_input("START YEAR:"))
					month = int(raw_input("START MONTH:"))
					day = int(raw_input("START DAY:"))
					finishDate = dt.date(year, month, day)
				self.books[count].endDate = finishDate
				return
		print "Could not find that title in %s." % self.name

	def removeBook(self, title):
		for count, book in self.books.items():
			if book.title == title:
				user_input = raw_input("Delete " + str(self.books[count]) + " (y/n)")
				if user_input == 'y':
					del self.books[count] 
				else:
					"Deletion operation cancelled."

class book(object):
	"""a book"""
	def __init__(self, title, author, pageCount, startDate="..."):
		self.title = title
		self.author = author
		self.pageCount = pageCount
		self.startDate = startDate
		self.endDate = "..."
		self.daysTaken = 0
		self.sessions = []
		self.currentPage = 0

	def finishedSession(self, sessionDate, sessionPageUpto):
		self.sessions.append((sessionDate, sessionPageUpto))
		self.currentPage = sessionPageUpto

	def timeTaken(self):
		if self.daysTaken > 0:
			return self.daysTaken
		elif self.endDate == "...":
			return "Book does not currently have an end date."
		else:
			self.daysTaken = self.endDate - self.startDate
			return self.daysTaken

	def __str__(self):
		return self.title + " - " + self.author + " [" + str(self.pageCount) + "pgs]" + " (" + str(self.startDate) + " to " + str(self.endDate) + ")" 


def bookHash(title, author, pageCount):
	"""takes in basic book details and returns a simple,
	readable form to identify book objects"""
	titleHash = "".join(item[0].lower() for item in title.split())
	authorHash = "".join(item[0].upper() for item in author.split())
	return authorHash + "_" + titleHash + "_" + pageCount

def getDate():
	year = int(raw_input("START YEAR:"))
	month = int(raw_input("START MONTH:"))
	day = int(raw_input("START DAY:"))
	return dt.date(year, month, day)

print "=" * 45
print "=" * 45
print "Welcome to the book tracker"

if os.path.isfile("my_books.pkl"):
	try:
		pkl_in = open('my_books.pkl', 'rb')
		My_Books = pickle.load(pkl_in) 
		pkl_in.close()
	except OSError:
		print "Problem loading from file"
else:
	My_Books = bookList("My Books")

user_input = ""

while user_input != 'e':
	print "-" * 55
	print 'n to add, l to list, s for session, f to finish, d to delete, e to exit'
	user_input = raw_input(":")
	if user_input == "n":
		title = raw_input("TITLE:")
		author = raw_input("AUTHOR:")
		pageCount = int(raw_input("NUMBER OF PAGES:"))
		user_input = raw_input("STARTED TODAY (y/n)?")
		if user_input == 'y':
			startDate = dt.date.today()
		else:
			startDate = getDate()
		newBook = book(title, author, pageCount, startDate)
		My_Books.addBook(newBook)
	if user_input == 'd':
		title = raw_input("TITLE TO DELETE:")
		My_Books.removeBook(title)
	if user_input == 's':
		user_input = raw_input("SESSION WAS TODAY (y/n)?")
		if user_input == 'y':
			sessionDate = dt.date.today()
		else:
			sessionDate = getDate()
		pageUpTo = int(raw_input("PAGE UP TO:"))
		My_Books.addSession(sessionDate, pageUpTo)
	if user_input == 'f':
		title = raw_input("TITLE:")
		My_Books.finishBook(title)
	if user_input == 'l':
		My_Books.listBooks()
	if user_input == 'e':
		pkl_out = open('my_books.pkl', 'wb')
		pickle.dump(My_Books, pkl_out)
		pkl_out.close()	
		exit
		
