"""
    Reviews Model
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column, ForeignKey
from base import Base

class Review(Base):
    """
    Reviews class:
        ID - Book id
        text - review detail
        book_id - id of the book
        student_id - owner of the review
    """
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(250), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    book = relationship('Book', back_populates='reviews')
    student = relationship('Student', back_populates='reviews')


    def __repr__(self):
        return f"<Review text = {self.text}>"
