#!/usr/bin/python3

import cmd
from rich import print
from models.students import Student
from models.books import Book
from models.reviews import Review
from utils import Util

class LibraryCli(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = "(lib)# "
        self.intro = "[italic red]*** Welcome ***\nLibrary Management Sys Admin\n"
        self.util = Util()


    def do_list(self, arg):
        """ List Items from the databases """
        if arg:
            cls = arg
            self.util.print_items(cls)
        else:
            print("Usage: list <classname>")
    
    def do_add(self, arg):
        """ Adds items to the database"""
        if arg:
            cls = arg
            self.util.add_item(cls)
        else:
            print("Usage: add <classname>")

    def do_quit(self, arg):
        """Ends the Program"""
        self.util.close_db()
        print("*** GoodBye ***")
        return True

if __name__ == '__main__':
    cli = LibraryCli()
    cli.cmdloop()
