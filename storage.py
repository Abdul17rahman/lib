"""
    Database storage class
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base import Base
from models.students import Student
from models.books import Book
from models.reviews import Review


class DbStorage(Base):
    path
    user
    password
    db_name

    def __init__(self):
        engine = create_engine(PATH, pool_pri_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

    def add(self):
        new_student = Student(first_name='Abdul', last_name='Rahman', email='abdu@email.com')
        print(new_student)
