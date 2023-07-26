from unittest import TestCase, main
from main import Main

class TestMain(TestCase):
    
    def testIncrement1(self):
        obj = Main(1, 2)

        self.assertEqual(obj.increment1(), 2)
        self.assertEqual(obj.localAttribute2, 2)

if __name__ == '__main__':
    main()