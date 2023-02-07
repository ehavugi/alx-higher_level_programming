#!/usr/bin/python3

"""
My list module with MyList class

"""


class MyList(list):
    """
    Class added printed_sorted method to normal list
    """

    def print_sorted(self):
        """
        prints a sorted listed without having to changing the list

        """
        print(sorted(self))
