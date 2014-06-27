#### Basic Book Tracker

###stage One
 - title
 - author
 - start date
 - end date

###stage Two
 - page count
 - start end Delta
 - code smoothing
 - description


###stage x
 - review
 - genre
 - time not just raw date
 - web scraping
 - purchase information
 - dealing with repeat entries
 - allow books to be entitires by themselves not inherent to a list
 - hash title/author for quick searching
 - single author multiple books

#known issues
 - test cases needed
 - streamline date entry
 - time taken print formatting
 - replace bookCount with uID
 - roll up statistics and timeTaken
 - import matlab


 #rev history
  - 1.7 - streamlined date input, added instructions with an input catch to avoid mass printing after every action
  - 1.6 - added few basic test cases
  - 1.5 - added check for duplicate items
  - 1.4 - fixed troublesome datetime bug in statistics due to function returning a string!
  - 1.3 - started adding list statistics, timeDeltas doesn't work
  - 1.2 - added listing of books with the time taken to read
  - 1.1 - added abilty to edit books
  - 1.0 - refactored file input and loop, removed os dependency, added uID, added SystemExit
  - 0.9 - elaborated the session code, tried to pretend i didn't need to make a database...
  - 0.8 - bookHash added (prelim), input of date moved to a function
  - 0.7 - expanded out session useage
  - 0.6 - added beginnings to session recording
  - 0.5 - added pagcount, time delta beginnings
  - 0.4 - added bookList class
  - 0.3 - added actual datetime objects for start / end
  - 0.2 - added book deletion, formatting and flow adjustments
  - 0.1 - basic list, file i/o, author title, start & finish date (string)



