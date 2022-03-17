from user import User
import json
import hashlib
from apiHandler import RequestHandler

class ManageUser:
    __user = None
    
    def __init__(self):
        ManageUser.__user = None
        self.__jsonFile = "users.json"
    
    #fetching user data from json file(database) and return in python dict
    def __getUsersData(self):
        try:
            with open(self.__jsonFile) as file:
                db = json.load(file)
            if "user" in db:
                return db["user"]
        except Exception as e:
            raise Exception("Unable to read json file.")
        else:
            return None
    #write users data to json file(database)
    def __setUsersData(self,data:list):
        try:
            with open(self.__jsonFile,"w") as file:
                db = {}
                db["user"]=data
                json.dump(db,file,indent=2)
        except Exception as e:
            raise Exception("Unable to write json file.")
    #create hash with sha256 and return hash
    def __getHash(self,passkey:str):
        return hashlib.sha256(str.encode(passkey)).hexdigest()
    
    #display all users in database
    def allUsers(self):
        if self.__user:
            db = self.__getUsersData()
            if db:
                print("Users:")
                for user in db:
                    if user["username"]: print(user["username"])
            else:
                raise Exception("Unable to fetch user data")
        else:
            raise Exception("Please login first.")
    
    #login with required username and passkey if exist in database
    def login(self,username:str,passkey:str):
        if self.checkLoginStatus():
            return
        if username and passkey:
            db = self.__getUsersData()
            if db:
                uname, uhash = None, None
                for user in db:
                    if user["username"] == username:
                        uname = user["username"]
                        uhash = user["passkey"]
                        break
                if uname:
                    passkey = self.__getHash(passkey)
                    if uname == username and uhash == passkey:
                        try:
                            ManageUser.__user = User()
                            ManageUser.__user.setUserName(username)
                            # ManageUser.__user.setPassKey(passkey)
                            self.__setCookie(self.__user.getUserName())
                        except Exception as e:
                            raise Exception(e)
                        else:
                            print(f"{self.__user.getUserName()}, Successfully logged In.")
                    else:
                        raise Exception("Invalid username or password.")
                else:
                    raise Exception("User Not Found")
            else:
                raise Exception("Unable to fetch user data")
        else:
            raise Exception("Login Failed: Please check username or password.")
    
    #logout if logged in already
    def logout(self):
        if self.__user:
            try:
                ManageUser.__user = None
                self.__setCookie(None)
            except Exception as e:
                raise Exception(e)
            else:
                print("Successfully Logged Out")
        else:
            raise Exception("Please login first.")
    
    #create user and add to database
    def createUser(self,username:str,passkey:str):
        if self.__user:
            try:
                db = self.__getUsersData()
                uname = None
                for user in db:
                    if user["username"]==username:
                        uname = user["username"]
                        break
                if not uname:
                    passkey = self.__getHash(passkey)
                    user = {}
                    user["username"]=username
                    user["passkey"]=passkey
                    db.append(user)
                    self.__setUsersData(db)
                else:
                    raise Exception(f"User {uname} already exist.")
            except Exception as e:
                raise Exception(e)
            else:
                print(f"User {username}, successfully created.")
        else:
            raise Exception("Please login first.")
    #update user in database
    def updateUser(self,username:str,oldpasskey:str,newusername:str=None,newpasskey:str=None):
        if self.__user:
            try:
                db = self.__getUsersData()
                if newusername or newpasskey:
                    update = False
                    for user in db:
                        if user["username"]==username:
                            uname = user["username"]
                            uhash = user["passkey"]
                            oldpasskey = self.__getHash(oldpasskey)
                            if uname == username and uhash == oldpasskey:
                                try:
                                    if newpasskey:
                                        newpasskey = self.__getHash(newpasskey)
                                        user["passkey"]=newpasskey
                                        update = True
                                    if newusername:
                                        if self.userExist(newusername):
                                            raise Exception(f"User {newusername} already exist.")
                                        else:
                                            user["username"]=newusername
                                            #if target user is currently logged in
                                            if self.__user.getUserName() == username:
                                                ManageUser.__user.setUserName(user["username"])
                                                self.__setCookie(self.__user.getUserName())
                                            username=user["username"]
                                            update = True
                                        
                                except Exception as e:
                                    raise Exception(e)
                            break
                    if update:
                        self.__setUsersData(db)
                        print(f"{username}, Successfully Updated.")
                    else:
                        raise Exception("Update Failed.")
                else:
                    raise Exception("new values missing.")
            except Exception as e:
                raise Exception(e)
        else:
            raise Exception("Please login first.")
    #delete user from database
    def deleteUser(self,username:str):
        if self.__user:
            try:
                if not username:
                    raise Exception("username value missing.")
                db = self.__getUsersData()
                userIndex = -1
                for i in range(len(db)):
                    if db[i]["username"] == username:
                        userIndex = i
                        break
                if userIndex != -1:
                    db.pop(userIndex)
                    self.__setUsersData(db)
                    print(f"{username}, Deletion Successful.")
                    #if target user is currently logged in
                    if self.__user.getUserName() == username:
                        self.logout()
                else:
                    raise Exception(f"{username}, does not exist.")
            except Exception as e:
                raise Exception(e)
        else:
            raise Exception("Please login first.")
    #check user currently logged in or not from cookie
    def checkLoginStatus(self):
        try:
            with open("temp.json") as f:
                cookie = json.load(f)
            username = None
            username = cookie["username"]
        except Exception as e:
            raise Exception(e)
        finally:
            if username:
                return username
            else:
                return None
        
    #get api response from cityName, stateCode or countryCode
    def getRequestByCityName(self,cityName:str,stateCode:str=None,countryCode:str=None):
        if self.__user:
            try:
                req = RequestHandler()
                rData = req.getRequestByCityName(cityName,stateCode,countryCode)
                res = req.getResponseData(rData)
                for key,val in res.items():
                    print(key,":",val)
            except Exception as e:
                raise Exception(e)
            finally:
                del req
        else:
            raise Exception("Please login first.")
    #get api response from latitude and longitude
    def getRequestByLatLon(self,lat:str,lon:str):
        if self.__user:
            try:
                req = RequestHandler()
                rData = req.getRequestByCityName(lat,lon)
                res = req.getResponseData(rData)
                for key,val in res.items():
                    print(key,":",val)
            except Exception as e:
                raise Exception(e)
            finally:
                del req
        else:
            raise Exception("Please login first.")
    #set cookie with username
    def __setCookie(self,username:str):
        try:
            with open("temp.json","w") as f:
                cookie = {}
                cookie["username"]=username
                json.dump(cookie,f,indent=2)
        except Exception as e:
            raise Exception("Failed to set cookie.",e)
    #update session
    def updateSession(self,username:str):
        try:
            if username and self.checkLoginStatus() == username:
                ManageUser.__user = User()
                ManageUser.__user.setUserName(username)
            else:
                raise Exception("username required.")
        except Exception as e:
            raise Exception("Session Update Failed.",e)
    #check username already taken or not
    def userExist(self,username):
        if self.__user:
            db = self.__getUsersData()
            if db:
                for user in db:
                    if user["username"]==username:
                        return True
                return False
        else:
            raise Exception("Please login first.")
