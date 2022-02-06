class Book:
    author = ""
    title = ""

    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print("\""+self.title+", written by "+self.author+"\"")

object1 = Book("John Steinbeck", "Of Mice and Men")
object1.display()

object2 = Book("Haper Lee", "To Kill a Mockingbird")
object2.display()

if __name__ == "__main__":
    pass