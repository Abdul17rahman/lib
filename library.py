#!/usr/bin/python3

import cmd
from models.students import Student
from models.books import Book
from models.reviews import Review
from storage import DbStorage

class LibraryCli(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = "$$$ "
        self.intro = "*** Welcome ***\nLibrary Management Sys Admin\n"
        self.db_storage = DbStorage()


    def do_list(self, arg):
        books = self.db_storage.all(Book)
        for book in books:
            print(f"Title: {book.title} \n Author: {book.author}\n Status: {book.status}")

    def do_quit(self, arg):
        """Ends the Program"""
        self.db_storage.close_connection()
        print("*** GoodBye ***")
        return True

if __name__ == '__main__':
    cli = LibraryCli()
    cli.cmdloop()
