import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user1 = User()
        self.user2 = User()
    def test_getUserName(self):
        self.assertEqual(self.user1.getUserName(),None)
        self.assertEqual(self.user2.getUserName(),None)
        self.user1.setUserName("sanjul")
        self.user2.setUserName(None)
        self.assertEqual(self.user1.getUserName(),"sanjul")
        self.assertEqual(self.user2.getUserName(),None)
    def test_setUserName(self):
        self.assertEqual(self.user1.setUserName("sanjul"),None)
        self.assertEqual(self.user2.setUserName(None),None)
        self.assertEqual(self.user1.getUserName(),"sanjul")
        self.assertEqual(self.user2.getUserName(),None)
    def test_setPassKey(self):
        self.assertEqual(self.user1.setPassKey("password"),None)
        self.assertEqual(self.user2.setPassKey(None),None)
        self.assertEqual(self.user1.getPassKey(),"password")
        self.assertEqual(self.user2.getPassKey(),None)
    def test_getPassKey(self):
        self.assertEqual(self.user1.getPassKey(),None)
        self.assertEqual(self.user2.getPassKey(),None)
        self.user1.setPassKey("password")
        self.user2.setPassKey(None)
        self.assertEqual(self.user1.getPassKey(),"password")
        self.assertEqual(self.user2.getPassKey(),None)
if __name__ == "__main__":
    unittest.main()