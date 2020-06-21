class Pro:
    def __init__(self):
        self._protectedVar = 0

class Pri:
    def __init__(self):
        self.__privateVar = 0
    def getValue(self):
        print(self.__privateVar)
    def setValue(self, value):
        self.__privateVar = value
        
if __name__ == "__main__":
    obj1 = Pro()
    obj2 = Pri()
    obj1._protectedVar = 45
    obj2.setValue(50)
    print(obj1._protectedVar)
    obj2.getValue()
