from LMS_DB import *

class Library:
    def __init__(self,title,author,publication_year):
        self.title=title
        self.author = author
        self.publication_year = publication_year
    def info(self):
        print(f"{self.title} by {self.author} published on {self.publication_year}")
class Book(Library):
    def __init__(self,title,author,publication_year,num_copies):
        super().__init__(title,author,publication_year)
        self.num_copies = num_copies
    def borrow_book(self):
        if self.num_copies > 0:
            self.num_copies-=1
            print(f"{self.title} borrowed successfully {self.num_copies} copies remaining")
        else:
            print(f"There are no more copies of {self.title} left")
    def return_book(self):
        print(f"{self.title} returned successfully")
        self.num_copies+=1
    def addToDB(self):
        s = Session()
        #Getting author ID from authors table using name string
        fetch_author = s.query(AuthorTable).filter(AuthorTable.name == self.author).first()
        if fetch_author:
            author_ID = fetch_author.id
        else:
            newAuthor = AuthorTable(name = self.author,booksID = [BookTable(id = 123)])
            s.add(newAuthor)
            author_ID = newAuthor.id
        newBook = BookTable(title = self.title, authorID = author_ID,publication_year = self.publication_year,num_copies = self.num_copies) #Add pub year and num copies
        s.add(newBook) 
        s.commit()
class Ebook(Library):
    def __init__(self,title,author,publication_year,file_format):
        super().__init__(title,author,publication_year)
        self.file_format = file_format
    def download_ebook(self):
        file_name = self.title.replace(" ","_")
        print(f"{file_name}.{self.file_format} is ready to download")


b1 = Book("Harry potter and the chamber of secreats","J.K. rowling","June 2 1999",5)
b1.info()
b1.borrow_book()
b1.return_book()

e1 = Ebook("Harry potter and the chamber of secreats","J.K. rowling","June 2 1999","kindle")
e1.info()
e1.download_ebook()


# homework
# class for student: attributes ex: name, department, # of books authorized, account details
