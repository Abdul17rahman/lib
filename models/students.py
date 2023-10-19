"""
    Students Model
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column
from models.base import Base


class Student(Base):
    """
    Student class:
        ID - Student's id
        first_name - Student's first name
        last_name - Student's last name
        email - Student's email
    """
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    books = relationship('Book', back_populates='student')
    reviews = relationship('Review', back_populates='student')


    def __repr__(self):
        return f"<Student name = {self.first_name} {self.last_name} email = {self.email}>"
