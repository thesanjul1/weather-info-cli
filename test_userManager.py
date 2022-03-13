from userManager import ManageUser
import unittest
import json

class TestManageUser(unittest.TestCase):
    def setUp(self):
        self.mgr = ManageUser()
        with open("temp.json","w") as f:
                cookie = {}
                cookie["username"]=None
                json.dump(cookie,f,indent=2)
    #user should be logged in to perform any activity except login
    def test_allUsers(self):
        with self.assertRaises(Exception):
            self.mgr.allUsers()
    def test_login(self):
        with self.assertRaises(Exception):
            self.mgr.login("testnosuchuser","testnosuchpassword")
            self.mgr.login(None,"testnosuchpassword")
    def test_logout(self):
        with self.assertRaises(Exception):
            self.mgr.logout()
    def test_createUser(self):
        with self.assertRaises(Exception):
            self.mgr.createUser("dummyusername","dummypassword")
            self.mgr.createUser("dummyusername",None)
            self.mgr.createUser("None","dummypassword")
    def test_updateUser(self):
        with self.assertRaises(Exception):
            self.mgr.updateUser("dummyusername","dummyoldpassword","dummynewusername","dummynewpassword")
            self.mgr.updateUser(None,"dummyoldpassword","dummynewusername","dummynewpassword")
            self.mgr.updateUser("dummyusername",None,"dummynewusername","dummynewpassword")
            self.mgr.updateUser("dummyusername","dummyoldpassword",None,None)
    def test_deleteUser(self):
        with self.assertRaises(Exception):
            self.mgr.deleteUser("sanjul")
            self.mgr.deleteUser(None)
    def test_checkLoginStatus(self):
        with open("temp.json") as f:
            res = json.load(f)["username"]
        self.assertEqual(self.mgr.checkLoginStatus(),res)
    def test_getRequestByCityName(self):
        with self.assertRaises(Exception):
            self.mgr.getRequestByCityName(None,None,None)
            self.mgr.getRequestByCityName("London",None,None)
    def test_getRequestByLatLon(self):
        with self.assertRaises(Exception):
            self.mgr.getRequestByLatLon(None,None)
            self.mgr.getRequestByLatLon(36,138)
            self.mgr.getRequestByLatLon("36","136")
    def test_updateSession(self):
        with self.assertRaises(Exception):
            self.mgr.updateSession(None)
            self.mgr.updateSession("dummyusername")

if __name__ == "__main__":
    unittest.main()