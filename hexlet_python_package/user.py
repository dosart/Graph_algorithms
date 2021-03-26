# -*- coding:utf-8 -*-

"""User representation."""


class User(object):
    """Object representation of user."""

    def __init__(self, name: str, age: int):
        """
        Construct a new user.

        Args:
            name: user's name
            age: user's age
        """
        self.name = name
        self.age = age

    def get_introduction(self) -> str:
        """
        Return a user's self-introduction.

        Returns:
            str
        """
        return "Hello, i'm {self.name}, {self.age}".format(self=self)
