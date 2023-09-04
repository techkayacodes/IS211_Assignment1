# Create a class called Book
class Book:
    # Initialize attributes author and title to blank strings
    def __init__(self, author="", title=""):
        self.author = author
        self.title = title

    # A function to display the book's information
    def display(self):
        print(f"{self.title}, written by {self.author}")

# Instantiate two objects from the Book class
book1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
book2 = Book("Walter Scott", "Ivanhoe: A Romance")

# Print both objects by calling their display() functions
book1.display()
book2.display()