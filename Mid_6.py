class Library:
    book_list=[]
    @classmethod
    def entry_book(cls,book):
        cls.book_list.append(book)
        
class Book:
    def __init__(self,book_id,title,author,availability=True):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.availability=availability
        Library.entry_book(self)

    def borrow_book(self):
        if self.availability:
            self.availability=False
            print(f"'{self.title}' Borrowed.")
        else:
            print(f"'{self.title}' Unavailable.")
    def return_book(self):
        if not self.availability:
            self.availability=True
            print(f"'{self.title}' Returned and Available.")
        else:
            print(f"'{self.title}' Not Borrowed, Cannot be Returned.")
    def view_book_info(self):
        availability_status="Available" if self.availability else "Unavailable"
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Availability: {availability_status}")

    def __repr__(self):
        return (f"Book(book_id={self.book_id}, title='{self.title}', "
                f"author='{self.author}', availability={self.availability})")
