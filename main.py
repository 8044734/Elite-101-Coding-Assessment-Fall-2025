from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def available_Books(library_books: list[dict]) -> list[dict]:
    available_Books = []
    for book in library_books:
      if book["available"] == True:
       "id": book["id"]
      "title": book["title"]
      "author": book["author"]

    return[available_Books]
# This code tells about the function of books that are available

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_Books(library_Books: list[dict]) -> list[dict]:
    search_Books = []
    author.lower
    genre.lower
    return[search_Books]
# This code tells about the function of searching books by author or genre

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
    

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
  

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

    if __name__ == "__main__":
    # You can use this space to test your functions
     pass