import requests
import json
class RequestHandler:
    #fetch secret api key from apikey.json file with appid as KEY and apikey as VALUE
    def __init__(self):
        with open("apikey.json") as f:
            data = json.load(f)
            if data["appid"]:
                self.appid = data["appid"]
            else:
                raise Exception("Missing aappid as KEY and apikey as VALUE in apikey.json file.")
    #weather information by cityname, statecode, countrycode
    def getRequestByCityName(self,cityName:str,stateCode:str=None,countryCode:str=None):
        cityName = (cityName if cityName else "")
        stateCode = (","+stateCode if stateCode else "")
        countryCode = (","+countryCode if countryCode else "")
        if cityName:
            try:
                PARAMS = {"q":cityName + stateCode + countryCode, 
                          "appid":self.appid}
                URL = "https://api.openweathermap.org/data/2.5/weather"
                r = requests.get(url=URL,params=PARAMS)
                rData = r.json()
            except Exception as e:
                raise Exception("Unable to precess request.")
            return rData
        else:
            raise Exception("Valid cityName and stateCode or countryCode required.")
    #weather information by latitude and longitude
    def getRequestByLatLon(self,lat:str,lon:str):
        if lat and lon:
            try:
                PARAMS = {"lat":lat,
                          "lon" :lon,
                          "appid":self.appid}
                URL = "https://api.openweathermap.org/data/2.5/weather"
                r = requests.get(url=URL,params=PARAMS)
                rData = r.json()
            except Exception as e:
                raise Exception("Unable to precess request.")
            return rData
        else:
            raise Exception("Valid lat,lon required.")
    #filter only required data to display in dict data
    def getResponseData(self,rData:dict):
        if rData:
            res = {}
            res["city"]=rData["name"]
            res["country"]=rData["sys"]["country"]
            res["humidity"]=rData["main"]["humidity"]
            res["average temperature"]=rData["main"]["temp"]
            res["pressure"]=rData["main"]["pressure"]
            res["wind speed"]=rData["wind"]["speed"]
            res["wind degree"]=rData["wind"]["deg"]
            return res
        else:
            raise Exception("Response data required.")