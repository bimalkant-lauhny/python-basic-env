from mod1 import Mod1

class Main:
    staticAttribute = []

    def __init__(self, arg1, arg2):
        self.localAttribute1 = arg1
        self.localAttribute2 = arg2
        self.importedAttribute = Mod1()
   
    def localMethod1(self):
        print(self.importedAttribute.attr2)

    def _privateLocalMethod(self):
        self.localAttribute2 += 1
    
    def increment1(self):
        self.__privateIncrement1()
        return self.localAttribute1

    def __privateIncrement1(self):
        self.localAttribute1 += 1


if __name__ == '__main__':
    mainObject = Main(1, 2)
    mainObject.localMethod1()