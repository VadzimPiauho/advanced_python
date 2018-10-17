class YourMetaClass(type):
    def __init__(cls, name, bases, attrs):
        prefixes = ["get_", "set_", "del_"]
        accessors = {}
        for key in attrs.keys():
            value = getattr(cls, key)

            if not callable(value):
                continue

            for i in range(len(prefixes)):
                if key.startswith(prefixes[i]):
                    accessors.setdefault(key[4:], [None, None, None])[i] = value    # noqa
        for name, (getter, setter, deleter) in accessors.items():
            setattr(cls, name, property(getter, setter, deleter, f"{name} property"))    # noqa


class Example(metaclass=YourMetaClass):
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return 'y'


ex = Example()
ex.x = 255
print(ex.x)
print(ex.y)
