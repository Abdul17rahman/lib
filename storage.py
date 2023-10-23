"""
    Database storage class
"""

import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base import Base
from models.students import Student
from models.books import Book
from models.reviews import Review

load_dotenv()

class DbStorage:

    def __init__(self):
        user = os.getenv('DB_USER')
        pswd = os.getenv('DB_PASSWD')
        host = os.getenv('DB_HOST')
        db = os.getenv('DB')
        PATH = f'mysql+mysqldb://{user}:{pswd}@{host}/{db}'

        self.engine = create_engine(PATH, pool_pre_ping=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def all(self, cls_name):
        """
        Returns data from the database
        """
        session = self.Session()
        return session.query(cls_name).all()

    def new(self, cls_name, **values):
        """
        This method adds data to the database.
        """
        session = self.Session()
        data = cls_name(**values)
        session.add(data)
        session.commit()

    def close_connection(self):
        session = self.Session()
        session.close()

"""
if __name__ == '__main__':
    # Add Students
    db_storage = DbStorage()
    session = db_storage.Session()
    students = [
        {
            'fname' : 'Birungi',
            'lname' : 'hadija',
            'email' : 'hady@email.com'
        },
        {
            'fname' : 'Ssiraje',
            'lname' : 'latifa',
            'email' : 'tee@email.com'
        },
        {
            'fname' : 'Naiga',
            'lname' : 'shakira',
            'email' : 'shaky@email.com'
        },
        {
            'fname' : 'Semanda',
            'lname' : 'hamza',
            'email' : 'ham@email.com'
        }
    ]
    
    for student in students:
        new_student = Student(first_name = student['fname'], last_name = student['lname'], email = student['email'])
        session.add(new_student)
        session.commit()
    print("Students successfully added")
    db_storage.new(Book, title='Master Java', author='Colt Steel')
    print("Book Added")
"""
