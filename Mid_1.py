class Library:
    book_list=[]
    @classmethod
    def entry_book(cls,book):
        cls.book_list.append(book)
        
# Example usage:
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __repr__(self):
        return f"Book(title='{self.title}',author='{self.author}')"
book1=Book("Zero To One","Peter Thiel")
book2=Book("Atomic Habits","James Clear")

Library.entry_book(book1)
Library.entry_book(book2)
print(Library.book_list)

