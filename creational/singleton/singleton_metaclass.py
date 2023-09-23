class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs) -> object:
        if cls not in cls.__class__._instances:
            cls.__class__._instances[cls] = super().__call__(*args, **kwargs)

        return cls.__class__._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self) -> None:
        print('Loading...')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()

    print(f'id(d1): {id(d1)}')
    print(f'id(d2): {id(d2)}')