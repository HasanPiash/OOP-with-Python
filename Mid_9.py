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
    def __str__(self):
        return f"Book[ID:{self.__book_id},Title:'{self.__title}',Author:'{self.__author}',Available:{self.__availability}]"
book=Book(101,"Zero To One","Peter Thiel",True)

print(book.book_id)
print(book.title)
print(book.author)
print(book.get_availability())
book.set_availability(False)
print(book.get_availability())
print(book)




# class Book:
#     def __init__(self,book_id,title,author,availability):
#         self.__book_id=book_id
#         self.__title=title
#         self.__author=author
#         self.__availability=availability
#     @property
#     def book_id(self):
#         return self.__book_id
#     @property
#     def title(self):
#         return self.__title
#     @property
#     def author(self):
#         return self.__author
#     @property
#     def availability(self):
#         return self.__availability
#     @availability.setter
#     def availability(self,value):
#         if type(value) is bool:
#             self.__availability=value
#         else:
#             print("Availability must be a boolean value.")
#     def __str__(self):
#         return f"Book[ID:{self.__book_id},Title:'{self.__title}',Author:'{self.__author}',Available:{self.__availability}]"

# book = Book(101, "Python Programming", "John Doe", True)

# print(book.book_id)
# print(book.title)
# print(book.author)
# print(book.availability)

# book.availability = False
# print(book.availability)

# print(book)




# class Book:
#     def __init__(self,book_id,title,author,availability):
#         self.__book_id=book_id
#         self.__title=title
#         self.__author=author
#         self.__availability=availability
#     def get_book_id(self):
#         return self.__book_id
#     def get_title(self):
#         return self.__title
#     def get_author(self):
#         return self.__author
#     def is_available(self):
#         return self.__availability
#     def set_availability(self,availability):
#         if type(availability) is bool:
#             self.__availability=availability
#         else:
#             print("Availability must be a boolean value.")
#     def __str__(self):
#         return f"Book[ID:{self.__book_id},Title:'{self.__title}',Author:'{self.__author}',Available:{self.__availability}]"

# book = Book(101, "Python Programming", "John Doe", True)
# print(book.get_book_id())
# print(book.get_title())
# print(book.get_author())
# print(book.is_available())
# book.set_availability(False)
# print(book.is_available())
# print(book)
# print(book)







# class Library:
#     book_list = []
#     @classmethod
#     def entry_book(cls, book):
#         cls.book_list.append(book)

#     @classmethod
#     def view_all_books(cls):
#         if cls.book_list:
#             print("\nList of Books in the Library:")
#             for book in cls.book_list:
#                 availability_status = "Available" if book.is_available() else "Unavailable"
#                 print(f"Book ID: {book.get_book_id()}, Title: {book.get_title()}, Author: {book.get_author()}, Availability: {availability_status}")
#         else:
#             print("\nNo books available in the library.")

#     @classmethod
#     def find_book(cls, book_id):
#         for book in cls.book_list:
#             if book.get_book_id() == book_id:
#                 return book
#         return None

# class Book:
#     def __init__(self, book_id, title, author, availability=True):
#         self.__book_id = book_id
#         self.__title = title
#         self.__author = author
#         self.__availability = availability
#         Library.entry_book(self)

#     def get_book_id(self):
#         return self.__book_id
#     def get_title(self):
#         return self.__title
#     def get_author(self):
#         return self.__author
#     def is_available(self):
#         return self.__availability

#     def borrow_book(self):
#         if self.__availability:
#             self.__availability = False
#             print(f"'{self.__title}' has been borrowed.")
#         else:
#             raise Exception(f"'{self.__title}' is currently unavailable for borrowing.")

#     def return_book(self):
#         if not self.__availability:
#             self.__availability = True
#             print(f"'{self.__title}' has been returned and is now available.")
#         else:
#             raise Exception(f"'{self.__title}' was not borrowed, so it cannot be returned.")

# # Menu-Driven System with Error Handling
# def menu():
#     while True:
#         print("\nLibrary Menu:")
#         print("1. View All Books")
#         print("2. Borrow Book")
#         print("3. Return Book")
#         print("4. Exit")
        
#         try:
#             choice = int(input("Enter your choice: "))
#         except ValueError:
#             print("Invalid input! Please enter a number between 1 and 4.")
#             continue

#         if choice == 1:
#             Library.view_all_books()
#         elif choice == 2:
#             book_id = input("Enter the Book ID to borrow: ")
#             book = Library.find_book(book_id)
#             if book:
#                 try:
#                     book.borrow_book()
#                 except Exception as e:
#                     print(f"Error: {e}")
#             else:
#                 print("Error: Invalid Book ID. Book not found!")
#         elif choice == 3:
#             book_id = input("Enter the Book ID to return: ")
#             book = Library.find_book(book_id)
#             if book:
#                 try:
#                     book.return_book()
#                 except Exception as e:
#                     print(f"Error: {e}")
#             else:
#                 print("Error: Invalid Book ID. Book not found!")
#         elif choice==4:
#             print("Exiting the library system. Goodbye!")
#             break
#         else:
#             print("Invalid choice! Enter a number 1 and 4.")

# # Adding some books for demonstration
# Book("101", "1984", "George Orwell")
# Book("102", "To Kill a Mockingbird", "Harper Lee")
# Book("103", "The Great Gatsby", "F. Scott Fitzgerald")


# menu()
