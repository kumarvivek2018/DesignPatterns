"""
There's a problem with this method that initializer still gets called
which may overwrite properties per instance creation call

It is not thread safe.
"""
import random


class Database:
    _instance = None

    def __init__(self):
        num = random.randint(1, 100)
        print(f'num: {num}')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()

    print(f'id(d1): {id(d1)}')
    print(f'id(d2): {id(d2)}')
