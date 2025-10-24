class Book:
    def __init__(self,book_id,title,author,availability):
        self.__book_id=book_id
        self.__title=title
        self.__author=author
        self.__availability=availability
        
    @property
    def book_id(self):
        return self.__book_id
    @property
    def title(self):
        return self.__title
    @property
    def author(self):
        return self.__author
    def get_availability(self):
        return self.__availability
    def set_availability(self,value):
        if type(value) is bool:
            self.__availability=value
        else:
            print("Availability must be a boolean value.")
    def borrow_book(self,book_id):
        if self.__book_id !=book_id:
            print("Error: Invalid book ID.")
            return
        if not self.__availability:
            print("Error: Book is Borrowed.")
            return
        self.__availability=False
        print(f"The book '{self.__title}' Borrowed successfully.")
    def return_book(self,book_id):
        if self.__book_id !=book_id:
            print("Error: Invalid book ID.")
            return
        if self.__availability:
            print("Error: The book was not borrowed.")
            return
        self.__availability=True
        print(f"The book'{self.__title}' returned successfully.")
    def __str__(self):
        return f"Book[ID:{self.__book_id},Title:'{self.__title}',Author:'{self.__author}',Available:{self.__availability}]"
book=Book(101,"Harry Potter","J.K.Rowling",True)
book.borrow_book(101)
book.borrow_book(101)
book.borrow_book(102)

book.return_book(101)
book.return_book(101)
book.return_book(102)
print(book)








# class Library:
#     book_list=[]
#     @classmethod
#     def entry_book(cls, book):
#         cls.book_list.append(book)

#     @classmethod
#     def view_all_books(cls):
#         if cls.book_list:
#             print("\nList of Books in the Library:")
#             for book in cls.book_list:
#                 availability_status="Available" if book.availability else "Unavailable"
#                 print(f"Book ID:{book.book_id}, Title:{book.title}, Author:{book.author}, Availability:{availability_status}")
#         else:
#             print("\nNo books available in the library.")

#     @classmethod
#     def find_book(cls,book_id):
#         for book in cls.book_list:
#             if book.book_id==book_id:
#                 return book
#         return None

# class Book:
#     def __init__(self,book_id,title,author,availability=True):
#         self.book_id=book_id
#         self.title=title
#         self.author=author
#         self.availability=availability
#         Library.entry_book(self)

#     def borrow_book(self):
#         if self.availability:
#             self.availability = False
#             print(f"'{self.title}' Borrowed.")
#         else:
#             raise Exception(f"'{self.title}' Unavailable for Borrowing.")
#     def return_book(self):
#         if not self.availability:
#             self.availability=True
#             print(f"'{self.title}' Returned and Available.")
#         else:
#             raise Exception(f"'{self.title}' Not Borrowed, Cannot be Returned.")
        
# def menu():
#     while True:
#         print("\nLibrary Menu:")
#         print("1. View All Books")
#         print("2. Borrow Book")
#         print("3. Return Book")
#         print("4. Exit")
        
#         try:
#             choice=int(input("Enter your choice: "))
#         except ValueError:
#             print("Invalid input! Enter a number between 1 and 4.")
#             continue

#         if choice==1:
#             Library.view_all_books()
#         elif choice==2:
#             book_id=input("Enter the Book ID to borrow: ")
#             book=Library.find_book(book_id)
#             if book:
#                 try:
#                     book.borrow_book()
#                 except Exception as e:
#                     print(f"Error: {e}")
#             else:
#                 print("Error: Book not found!")
#         elif choice==3:
#             book_id=input("Enter the Book ID to return: ")
#             book=Library.find_book(book_id)
#             if book:
#                 try:
#                     book.return_book()
#                 except Exception as e:
#                     print(f"Error: {e}")
#             else:
#                 print("Book not found!")
#         elif choice==4:
#             print("Exiting the library system")
#             break
#         else:
#             print("Invalid choice! Enter 1 and 4.")

# Book("101", "1984", "George Orwell")
# Book("102", "To Kill a Mockingbird", "Harper Lee")
# Book("103", "The Great Gatsby", "F. Scott Fitzgerald")

# menu()

