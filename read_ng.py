# read.ng - 1.1
# python 2.7

"""
book tracking app

"""

import cPickle as pickle
import datetime as dt 

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

	def editBook(self):
		title = raw_input("TITLE OF BOOK TO EDIT:")
		for count, book in self.books.items():
			if book.title == title:
				attribute = raw_input("ATTRIBUTE TO EDIT (title, author, pageCount):")
				newAttribute = raw_input("NEW VALUE:")
				if attribute == "pageCount":
					book.pageCount = int(newAttribute)
				elif attribute == "title":
					book.title = newAttribute
				elif attribute == "author":
					book.author = newAttribute
				else:
					"Invalid attribute selected"
				return
		print "Cannot find any book of that title in the list."

	def addSession(self, sessionDate, paegUpTo):
		currentBook = self.books[self.bookCount-1]
		if pageUpTo > currentBook.pageCount:
			print "That is more than the number of pages in %s" % str(currentBook)
		else:
			currentBook.finishedSession(sessionDate, pageUpTo)
			print str(currentBook)
			if 	currentBook.pageCount == pageUpTo:
				print "You have completed %s by %s." % (currentBook.title, currentBook.author)
				currentBook.endDate = dt.date.today()
			else:
				print "Currently up to page %s out of %s pages." % (currentBook.currentPage, currentBook.pageCount)

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
	def __init__(self, title, author, pageCount, uID, startDate="..."):
		self.title = title
		self.author = author
		self.pageCount = pageCount
		self.uID = uID
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
	return authorHash + "_" + titleHash + "_" + str(pageCount)

def getDate():
	year = int(raw_input("START YEAR:"))
	month = int(raw_input("START MONTH:"))
	day = int(raw_input("START DAY:"))
	return dt.date(year, month, day)

print "=" * 45
print "=" * 45
print "Welcome to the book tracker"

bookFile = "my_books.pkl"
try:
	pkl_in = open(bookFile, 'rb')
	My_Books = pickle.load(pkl_in) 
	pkl_in.close()
	print "Book data loaded from file %s." % bookFile
except IOError:
	print "Problem loading from file %s." % bookFile
	My_Books = bookList("My Books")


while True:
	print "*****************************************"
	print "***  1 - Add a new book"
	print "***  2 - Detail a new session" 		 
	print "***  3 - Finish reading a book"
	print "***  4 - List all books"
	print "***  5 - Edit a book"
	print "***  6 - Delete a book"
	print "***  0 - Save and exit"
	print "*****************************************"

	user_input = raw_input(":")

	if user_input == "1":
		title = raw_input("TITLE:")
		author = raw_input("AUTHOR:")
		pageCount = int(raw_input("NUMBER OF PAGES:"))
		user_input = raw_input("STARTED TODAY (y/n)?")
		if user_input == 'y':
			startDate = dt.date.today()
		else:
			startDate = getDate()
		uID = bookHash(title, author, pageCount)
		newBook = book(title, author, pageCount, uID, startDate)
		My_Books.addBook(newBook)

	if user_input == '2':
		user_input = raw_input("SESSION WAS TODAY (y/n)?")
		if user_input == 'y':
			sessionDate = dt.date.today()
		else:
			sessionDate = getDate()
		pageUpTo = int(raw_input("PAGE UP TO:"))
		My_Books.addSession(sessionDate, pageUpTo)
	
	if user_input == '3':
		title = raw_input("TITLE:")
		My_Books.finishBook(title)

	if user_input == '4':
		My_Books.listBooks()

	if user_input == '5':
		print "Editing book, currently listed:"
		My_Books.listBooks()
		My_Books.editBook()		

	if user_input == '6':
		title = raw_input("TITLE TO DELETE:")
		My_Books.removeBook(title)
	
	if user_input == '0':
		pkl_out = open(bookFile, 'wb')
		pickle.dump(My_Books, pkl_out)
		pkl_out.close()	
		print "Book data saved to file %s." % bookFile
		raise SystemExit
		exit
		
