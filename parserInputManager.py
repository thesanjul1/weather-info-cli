import argparse
from userManager import ManageUser
import getpass

class Manager:
    def __init__(self):
        self.__cmd = False
        self.__mgr = ManageUser()
        self.__username = None
        self.__inp = None
        self.__setInpParser()
    #adding arguments and creating parse_args object as __inp
    def __setInpParser(self):
        try:
            parser = argparse.ArgumentParser()
            self.__username = self.__mgr.checkLoginStatus()
            parser.add_argument("-u","--username",help=": Enter username to login (e.g: -u sanjul)",default=self.__username)
            parser.add_argument("-n","--create",help=": Enter new unique username (e.g: -n sanjul007)")
            parser.add_argument("-c","--update",help=": Enter username to change it's info (e.g: -c sanjul)")
            parser.add_argument("-d","--delete",
                                help=": Enter username to delete it (e.g: -d sanjul)")
            parser.add_argument("-a","--all",
                                help=": Enter TRUE or FALSE  to view all users (e.g: -a true)")
            parser.add_argument("-o","--logout",
                                help=": Enter TRUE or FALSE to logout (e.g: -o true)")
            parser.add_argument("-wc",
                                help=": Enter [CityName] [stateCode](optional) [countryCode](optional) to get Weather info (e.g: -wc London OR -wc London null OR -wc London null uk)",
                                nargs='+')
            parser.add_argument("-w",
                                help=": Enter [Latitude] [Longitude] to get Weather info (e.g: -w 35 139)",
                                nargs='+')
            self.__inp = parser.parse_args()
        except Exception as e:
            raise Exception("Failed to initialize Manager object:",e)
    #check option arguments are given or not
    def isUsername(self):
        if self.__username:
            return True
        else:
            return False
    def isCreate(self):
        if self.__inp and self.__inp.create:
            return True
        else:
            return False
    def isUpdate(self):
        if self.__inp and self.__inp.update:
            return True
        else:
            return False
    def isDelete(self):
        if self.__inp and self.__inp.delete:
            return True
        else:
            return False
    def isAll(self):
        if self.__inp and self.__inp.all:
            return True
        else:
            return False
    def isLogout(self):
        if self.__inp and self.__inp.logout:
            return True
        else:
            return False
    def isWeatherByCity(self):
        if self.__inp and self.__inp.wc:
            return True
        else:
            return False
    def isWeatherByLatLon(self):
        if self.__inp and self.__inp.w:
            return True
        else:
            return False
    def isCommand(self):
        if self.__cmd:
            return True
        else:
            return False
    # Handle when option arguments are given
    def respUsername(self):
        if self.__username:
            if self.__inp.username == self.__username:
                self.__mgr.updateSession(self.__username)
            else:
                raise Exception("Already logged in. Please logout first to login from another account.")
        else:
            if self.__inp.username:
                self.__cmd = True
                password = getpass.getpass()
                self.__mgr.login(self.__inp.username,password)
            else:
                raise Exception("Please login first.")
    def respCreate(self):
        if self.isCreate():
            self.__cmd = True
            password = getpass.getpass(prompt="New Password: ")
            self.__mgr.createUser(self.__inp.create,password)
    def respUpdate(self):
        if self.isUpdate():
            self.__cmd = True
            password = getpass.getpass(prompt="old password: ")
            print("[1] change username\t[2] change password\t(e.g: 2)")
            choice = input("Enter the choice number: ")
            if choice == "1":
                newname = input("Enter new username: ")
                self.__mgr.updateUser(self.__inp.update, password, newusername=newname,newpasskey=None)
            elif choice == "2":
                newpass = getpass.getpass(prompt="New Password: ")
                self.__mgr.updateUser(self.__inp.update, password, newusername=None,newpasskey=newpass)
            else:
                raise Exception("Sorry, invalid choice number.")
    def respDelete(self):
        if self.isDelete():
            self.__cmd = True
            self.__mgr.deleteUser(self.__inp.delete)
    def respAll(self):
        if self.isAll():
            self.__cmd = True
            if self.__inp.all.upper() == "TRUE":
                self.__mgr.allUsers()
            else:
                raise Exception("Invalid boolean value.")
    def respLogout(self):
        if self.isLogout():
            self.__cmd = True
            if self.__inp.logout.upper() == "TRUE":
                self.__mgr.logout()
            else:
                raise Exception("Invalid boolean value.")
    def respWeatherByCity(self):
        if self.isWeatherByCity():
            cmd = True
            if len(self.__inp.wc) == 1 and self.__inp.wc[0] != "null":
                self.__mgr.getRequestByCityName(self.__inp.wc[0],stateCode=None,countryCode=None)
            elif len(self.__inp.wc) == 2 and self.__inp.wc[0] != "null":
                self.__inp.wc[1] = self.__inp.wc[1] if self.__inp.wc[1] != "null" else None
                self.__mgr.getRequestByCityName(self.__inp.wc[0],stateCode=self.__inp.wc[1],countryCode=None)
            elif len(self.__inp.wc) == 3 and self.__inp.wc[0] != "null":
                self.__inp.wc[1] = self.__inp.wc[1] if self.__inp.wc[1] != "null" else None
                self.__inp.wc[2] = self.__inp.wc[2] if self.__inp.wc[2] != "null" else None
                self.__mgr.getRequestByCityName(self.__inp.wc[0],stateCode=self.__inp.wc[1],countryCode=self.__inp.wc[2])
            else:
                raise Exception("Invalid input list: CityName StateCode CountryCode",self.__inp.wc,len(self.__inp.wc))
    def respWeatherByLatLon(self):
        if self.isWeatherByLatLon():
            self.__cmd = True
            if len(self.__inp.w) == 2:
                if self.__inp.w[0] not in  ["null",None] and self.__inp.w[1] not in  ["null",None]:
                    self.__mgr.getRequestByLatLon(self.__inp.w[0],self.__inp.w[1])
                else:
                    raise Exception("Invalid values: lat & lon cannot be null.")
            else:
                raise Exception("Invalid input list: lat(required) lon(required)",self.__inp.w,len(self.__inp.w))
