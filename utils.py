"""
    This module contains utility methods for database manipulation
"""

from models.students import Student
from models.books import Book
from models.reviews import Review
from storage import DbStorage


class Util:
    def __init__(self):
        self.db_storage = DbStorage()
        self.session = self.db_storage.Session()

    def print_items(self, cls_name):
        """
        Prints the results from the Db
        """
        if cls_name.capitalize() == 'Book':
            books = self.session.query(Book).all()
            if not books:
                print("No books available")
                return
            for book in books:
                    print(f"Title: {book.title}")
                    print(f"Author: {book.author}")
                    if book.status == 'Taken':
                        print(f"Status: {book.status}")
                        print(f"Rented to: {book.taken_by}")
                    else:
                        print(f"Status: {book.status}")
        elif cls_name.capitalize() == 'Student':
            students = self.session.query(Student).all()
            if not students:
                print("Please add students")
                return
            for student in students:
                    print(f"[italic red]Name: {student.first_name} {student.last_name}")
                    print(f"Email: {student.email}")
                    if student.books:
                        print(f"--Current Books--")
                        for book in student.books:
                            print(f"Title: {book.title}")
                    if student.reviews:
                        print("=== Reviews left ===")
                        for r in student.reviews:
                            print(f"{r.book.title} -- {r.text}")
        elif cls_name.capitalize() == 'Review':
            reviews = self.session.query(Review).all()
            if not reviews:
                print("No reviews.")
                return
            for r in reviews:
                    print(f"Review: {r.text}")
                    print(f"On: {r.book.title}")
                    print(f"By: {r.student.first_name}")
        else:
            print(f"class {cls_name} not found!")

    def add_item(self, cls_name):
        """Adds data into the database"""
        if cls_name.capitalize() == 'Student':
            fname = input("Enter Fisrt name: ")
            lname = input("Enter Last name: ")
            email = input("Enter email: ")
            new_student = Student(first_name=fname, last_name=lname, email=email)
            self.session.add(new_student)
            self.session.commit()
            print(f"Student {fname} is added succesfully.")
        elif cls_name.capitalize() == 'Book'.capitalize():
            title = input("Book Title: ")
            author = input("Author: ")
            new_book = Book(title=title, author=author)
            self.session.add(new_book)
            self.session.commit()
            print(f"Book {title} Added")
        elif cls_name.capitalize() == 'Review'.capitalize():
            bk_title = input("Book Title: ")
            student = int(input("Student's ID: "))
            text = input("Review: ")
            stu_id = self.session.query(Student).filter(Student.id == student).first()
            bk_id = self.session.query(Book).filter(Book.title == bk_title).first()
            if not stu_id:
                print("Student doesnt exit")
                return
            if not bk_id:
                print("Book doesnt exit")
                return
            new_review = Review(text=text, student_id=stu_id.id, book_id=bk_id.id)
            self.session.add(new_review)
            self.session.commit()
            print(f"Thank you for rating {bk_id.title}")
        else:
            print(f"class {cls_name} not found!")

    def close_db(self):
        """Closes database connection"""
        self.db_storage.close_connection()
        return
