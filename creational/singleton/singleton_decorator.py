def singleton(cls):
    _instances = {}

    def wrap(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return wrap


@singleton
class Database:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self):
        return self._name


if __name__ == '__main__':
    d1 = Database('mongo')
    d2 = Database('mysql')

    print(f'id(d1): {id(d1)}')
    print(f'id(d2): {id(d2)}')

    print(f'd1.name: {d1.name}')
    print(f'd2.name: {d2.name}')
