class Object:
    def update(self):
        pass


class Subject:
    def __init__(self):
        self.__o = set()  # множество объектов (Object)

    def add_object(self, o: Object):
        self.__o.add(o)

    def remove_object(self, o: Object):
        self.__o.remove(o)

    def notify(self):
        for o in self.__o:
            o.update()
