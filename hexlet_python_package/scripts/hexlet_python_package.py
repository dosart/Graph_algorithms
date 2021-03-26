# -*- coding:utf-8 -*-

"""An example script."""

from hexlet_python_package import user


def main():
    """Run an example code."""
    # it is ok to have some magical numbers locally
    print(user.User(name='Bob', age=42).get_introduction())  # noqa:WPS432


if __name__ == '__main__':
    main()
