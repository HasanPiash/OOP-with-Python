class Library:
    books = [
        {"id": "101", "title": "Harry Potter", "author": "J.K. Rowling", "available": True},
        {"id": "102", "title": "Zero To One", "author": "Peter Thiel", "available": True},
        {"id": "103", "title": "Atomic Habuts", "author": "James Clear", "available": True},
    ]

    @classmethod
    def view_all_books(cls):
        if not cls.books:
            print("\nNo books available.")
            return

        print("\nAvailable Books:")
        print(f"{'ID':<6}{'Title':<25}{'Author':<20}{'Status':<10}")
        print("-"*60)
        for book in cls.books:
            status="Available" if book["available"]else "Borrowed"
            print(f"{book['id']:<6} {book['title']:<25} {book['author']:<20}{status}")
    @classmethod
    def borrow_book(cls, book_id):
        for book in cls.books:
            if book["id"]==book_id:
                if book["available"]:
                    book["available"]=False
                    print(f"\nBorrowed '{book['title']}'.")
                else:
                    print(f"\nSorry, '{book['title']}' Already Borrowed.")
                return
        print("\nBook ID not found.")
    @classmethod
    def return_book(cls, book_id):
        for book in cls.books:
            if book["id"]==book_id:
                if not book["available"]:
                    book["available"]=True
                    print(f"\nReturned '{book['title']}'.")
                else:
                    print(f"\n'{book['title']}' Not borrowed.")
                return
        print("\nBook ID not found.")
def menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice=input("Enter (1-4): ")
        if choice=="1":
            Library.view_all_books()
        elif choice=="2":
            book_id=input("Enter Borrow Book: ")
            Library.borrow_book(book_id)
        elif choice=="3":
            book_id=input("Enter Return Book: ")
            Library.return_book(book_id)
        elif choice=="4":
            print("Exiting.")
            break
        else:
            print("Invalid choice! Enter 1 and 4.")
menu()









# class Library:
#     book_list = []  # Class-level variable to store books
    
#     @classmethod
#     def entry_book(cls, book):
#         """Adds a book to the library."""
#         cls.book_list.append(book)
    
#     @classmethod
#     def view_all_books(cls):
#         """Displays all books in the library."""
#         if cls.book_list:
#             print("\nList of Books:")
#             print(f"{'Book ID':<10} {'Title':<25} {'Author':<20} {'Availability'}")
#             print("-" * 60)
#             for book in cls.book_list:
#                 availability_status = "Available" if book.availability else "Unavailable"
#                 print(f"{book.book_id:<10} {book.title:<25} {book.author:<20} {availability_status}")
#         else:
#             print("\nNo books available.")
    
#     @classmethod
#     def find_book(cls, book_id):
#         """Finds a book by its ID."""
#         for book in cls.book_list:
#             if book.book_id == book_id:
#                 return book
#         return None

# class Book:
#     def __init__(self, book_id, title, author, availability=True):
#         """Initializes a new book and adds it to the library."""
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.availability = availability
#         Library.entry_book(self)
    
#     def borrow_book(self):
#         """Marks the book as borrowed if available."""
#         if self.availability:
#             self.availability = False
#             print(f"'{self.title}' has been borrowed.")
#         else:
#             print(f"'{self.title}' is currently unavailable.")
    
#     def return_book(self):
#         """Marks the book as returned if it was borrowed."""
#         if not self.availability:
#             self.availability = True
#             print(f"'{self.title}' has been returned and is now available.")
#         else:
#             print(f"'{self.title}' was not borrowed, cannot be returned.")

# def menu():
#     """Menu-driven system to interact with the library."""
#     while True:
#         print("\nLibrary Menu:")
#         print("1. View All Books")
#         print("2. Borrow Book")
#         print("3. Return Book")
#         print("4. Exit")
        
#         try:
#             choice = int(input("Enter choice (1-4): "))
#         except ValueError:
#             print("Invalid input! Please enter a number between 1 and 4.")
#             continue

#         if choice == 1:
#             Library.view_all_books()
#         elif choice == 2:
#             book_id = input("Enter the Book ID to borrow: ").strip()
#             book = Library.find_book(book_id)
#             if book:
#                 book.borrow_book()
#             else:
#                 print("Book not found!")
#         elif choice == 3:
#             book_id = input("Enter the Book ID to return: ").strip()
#             book=Library.find_book(book_id)
#             if book:
#                 book.return_book()
#             else:
#                 print("Book not found!")
#         elif choice==4:
#             print("Exiting... Thank you!")
#             break
#         else:
#             print("Invalid choice! Please enter a number between 1 and 4.")

# Book("101", "1984", "George Orwell")
# Book("102", "To Kill a Mockingbird", "Harper Lee")
# Book("103", "The Great Gatsby", "F. Scott Fitzgerald")
# menu()







# # class Library:
# #     book_list=[]
# #     @classmethod
# #     def entry_book(cls, book):
# #         cls.book_list.append(book)
# #     @classmethod
# #     def view_all_books(cls):
# #         if cls.book_list:
# #             print("\nList of Books in the Library:")
# #             for book in cls.book_list:
# #                 availability_status="Available" if book.availability else "Unavailable"
# #                 print(f"Book ID:{book.book_id},Title:{book.title},Author:{book.author},Availability:{availability_status}")
# #         else:
# #             print("\nNo books available in the library.")
# #     @classmethod
# #     def find_book(cls,book_id):
# #         for book in cls.book_list:
# #             if book.book_id==book_id:
# #                 return book
# #         return None
# # class Book:
# #     def __init__(self,book_id,title,author,availability=True):
# #         self.book_id=book_id
# #         self.title=title
# #         self.author=author
# #         self.availability=availability
# #         Library.entry_book(self)
# #     def borrow_book(self):
# #         if self.availability:
# #             self.availability=False
# #             print(f"'{self.title}' Borrowed.")
# #         else:
# #             print(f"'{self.title}' Unavailable.")
# #     def return_book(self):
# #         if not self.availability:
# #             self.availability=True
# #             print(f"'{self.title}' Available.")
# #         else:
# #             print(f"'{self.title}' Not borrowed, Cannot be returned.")

# # # Menu-Driven System
# # def menu():
# #     while True:
# #         print("\nLibrary Menu:")
# #         print("1. View All Books")
# #         print("2. Borrow Book")
# #         print("3. Return Book")
# #         print("4. Exit")
        
# #         try:
# #             choice=int(input("Enter your choice: "))
# #         except ValueError:
# #             print("Invalid input! enter 1 and 4.")
# #             continue


# #         if choice==1:
# #             Library.view_all_books()
# #         elif choice==2:
# #             book_id=input("Book Borrow: ")
# #             book=Library.find_book(book_id)
# #             if book:
# #                 book.borrow_book()
# #             else:
# #                 print("Book not found!")
# #         elif choice == 3:
# #             book_id=input("Enter the Book ID to return: ")
# #             book=Library.find_book(book_id)
# #             if book:
# #                 book.return_book()
# #             else:
# #                 print("Book not found!")
# #         elif choice == 4:
# #             print("Exit")
# #             break
# #         else:
# #             print("Invalid! enter 1 and 4.")
# # # Adding some books for demonstration
# # Book("101", "1984", "George Orwell")
# # Book("102", "To Kill a Mockingbird", "Harper Lee")
# # Book("103", "The Great Gatsby", "F. Scott Fitzgerald")

# # menu()

