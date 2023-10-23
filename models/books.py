"""
    Books Model
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column, ForeignKey
from models.base import Base

class Book(Base):
    """
    Book class:
        ID - Book id
        title - Books title
        author - book author
        status - taken or available
    """
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    author = Column(String(30), nullable=False)
    status = Column(String(10), default='Available')
    taken_by = Column(Integer, ForeignKey('students.id'))
    student = relationship('Student', back_populates='books')
    reviews = relationship('Review', back_populates='book')


    def __repr__(self):
        return f"<Book name = {self.title} by = {self.author}>"
