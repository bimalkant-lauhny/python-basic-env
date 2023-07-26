from unittest import TestCase, main
from main import Main

class TestMain(TestCase):
    
    def setUp(self):
        """
        runs for every test case once
        """
        self.testMainObj = Main(1, 2)

    def testIncrement1(self):
        self.assertEqual(self.testMainObj.increment1(), 2)
        self.assertEqual(self.testMainObj.localAttribute2, 2)
    
    def testDecrement1(self):
        self.testMainObj.decrement2()
        self.assertEqual(self.testMainObj.localAttribute2, 1)

        self.testMainObj.decrement2()
        self.assertRaises(ValueError, self.testMainObj.decrement2)

if __name__ == '__main__':
    main()