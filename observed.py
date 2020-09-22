import weakref

class Object:
    def update(self):
        pass


class Subject:
    def __init__(self, objects=None):

        self.__o = weakref.WeakSet(objects) if objects is not None else set()  # множество объектов (Object)

    def add_object(self, o: Object):
        self.__o.add(o)

    def remove_object(self, o: Object):
        self.__o.remove(o)

    def notify(self):
        for o in self.__o:
            o.update()
