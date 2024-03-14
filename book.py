"""Task 1"""


class Book:
    """Book class"""

    def __init__(self, author, book_name, published_year, genre):
        self.author = author
        self.book_name = book_name
        self.published_year = published_year
        self.genre = genre

    def __str__(self):
        return (f"Author: {self.author}, Book: {self.book_name},"
                f" Published year: {self.published_year}, Genre: {self.genre}")

    def __repr__(self):
        return (f"Author: {self.author}, Book: {self.book_name},"
                f" Published year: {self.published_year}, Genre: {self.genre}")


book1 = Book("eugene", "python starter", 2024, "science")
book2 = Book("andrew", "python essential", 1991, "science")
book3 = Book("lola", "python advanced", 2017, "science")

books = [book1, book2, book3]

print(book1, book2, book3, end="\n")
print(books)

