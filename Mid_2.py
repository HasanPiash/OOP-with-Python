class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.availability=availability

    def __repr__(self):
        return(f"Book(book_id={self.book_id}, title='{self.title}', "
                f"author='{self.author}',availability={self.availability})")
        
