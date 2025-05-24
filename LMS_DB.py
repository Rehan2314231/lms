from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine("sqlite:///lms.db")

Base = declarative_base()

class BookTable(Base):
    __tablename__ = "books"
    id = Column(Integer,primary_key = True)
    title = Column(String)
    authorID = Column(Integer, ForeignKey("authors.id"))
    author = relationship("AuthorTable") #Because of 2 way relationship      ,back_populates = "booksID"
    publication_year = Column(Integer)
    num_copies = Column(Integer)



class AuthorTable(Base):
    __tablename__ = "authors"
    id = Column(Integer,primary_key = True)
    name = Column(String)
    booksID = relationship("BookTable",back_populates = "author")#Because of 2 way relationship,1 to many relationship



# table creation
    
Base.metadata.create_all(engine)
print("Tables created successfuly")

############################################################

#record creation
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = engine)
s = Session()
newAuthor = AuthorTable(name = "Stephen King")
s.add(newAuthor)
s.commit()


# make a new record for book table