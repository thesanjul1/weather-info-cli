from apiHandler import RequestHandler
import unittest
from unittest.mock import patch

class TestRequestHandler(unittest.TestCase):
    def setUp(self):
        self.req = RequestHandler()
    
    def test_getRequestByCityName(self):
        with self.assertRaises(Exception):
            self.req.getRequestByCityName(None,stateCode=None,countryCode=None)
            self.req.getRequestByCityName(None,stateCode="wrongInput",countryCode="wrongInput")
            self.req.getRequestByCityName("wrongInput",stateCode=None,countryCode=None)
            
    def test_getRequestByLatLon(self):
        with self.assertRaises(Exception):
            self.req.getRequestByLatLon(None,None)
            self.req.getRequestByLatLon("36",None)
            self.req.getRequestByLatLon(None,"156")
            self.req.getRequestByLatLon(36,"156")
    def test_getResponseData(self):
        with self.assertRaises(Exception):
            self.req.getResponseData(20)
            self.req.getResponseData({"demo":"example"})

if __name__ == "__main__":
    unittest.main()