from threading import Thread, Lock

class LockedClass:
    lock = Lock()
    def __init__(self):
        with self.lock:
            self.__first_name = ""
            pass
    @property
    def __first_name():
        print("e343")
    @classmethod
    @__first_name.setter
    def __first_name(self, name):
        with self.lock:
            print("My Name is")
