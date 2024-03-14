"""Task 1"""


class Book:
    """Book class"""

    def __init__(self, author, book_name, published_year, genre):
        self.author = author
        self.book_name = book_name
        self.published_year = published_year
        self.genre = genre
        self.reviews = []

    def __str__(self):
        return (f"Author: {self.author}, Book: {self.book_name},"
                f" Published year: {self.published_year},"
                f" Genre: {self.genre}, reviews: {self.reviews}")

    def __repr__(self):
        return (f"Author: {self.author}, Book: {self.book_name},"
                f" Published year: {self.published_year},"
                f" Genre: {self.genre}, reviews: {self.reviews}")


class Review:
    """Review for task 2"""

    @staticmethod
    def add_review_to_book(book: Book, text_review) -> None:
        book.reviews.append(text_review)


book1 = Book("eugene", "python starter", 2024, "science")
book2 = Book("andrew", "python essential", 1991, "science")
book3 = Book("lola", "python advanced", 2017, "science")

books = [book1, book2, book3]

my_review_for_book1 = Review.add_review_to_book(book1, "very good book")
my_review_for_book2 = Review.add_review_to_book(book2, "fascinating")
my_review_for_book3 = Review.add_review_to_book(book3, "very interesting")
my_review_for_book3_1 = Review.add_review_to_book(book3, "great book")

print(book1, book2, book3, end="\n")
print(books)

