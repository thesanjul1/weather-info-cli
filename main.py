import argparse
from userManager import ManageUser
import getpass

def main():
    try:
        cmd = False
        mgr = ManageUser()
        parser = argparse.ArgumentParser()
        username = mgr.checkLoginStatus()
        parser.add_argument("-u","--username",help=": Enter username to login (e.g: -u sanjul)",default=username)
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
        inp = parser.parse_args()
        # print(inp.username)
        if username:
            if inp.username == username:
                mgr.updateSession(username)
            else:
                raise Exception("Already logged in. Please logout first to login from another account.")
        else:
            if inp.username:
                cmd = True
                password = getpass.getpass()
                mgr.login(inp.username,password)
            else:
                raise Exception("Please login first.")
        # print(inp.create)
        if inp.create:
            cmd = True
            password = getpass.getpass(prompt="New Password: ")
            mgr.createUser(inp.create,password)
        # print(inp.update)
        if inp.update:
            cmd = True
            password = getpass.getpass(prompt="old password: ")
            print("[1] change username\t[2] change password\t(e.g: 2)")
            choice = input("Enter the choice number: ")
            if choice == "1":
                newname = input("Enter new username: ")
                mgr.updateUser(inp.update, password, newusername=newname,newpasskey=None)
            elif choice == "2":
                newpass = getpass.getpass(prompt="New Password: ")
                mgr.updateUser(inp.update, password, newusername=None,newpasskey=newpass)
            else:
                raise Exception("Sorry, invalid choice number.")
        # print(inp.delete)
        if inp.delete:
            cmd = True
            mgr.deleteUser(inp.delete)
        # print(inp.all)
        if inp.all:
            cmd = True
            if inp.all.upper() == "TRUE":
                mgr.allUsers()
            else:
                raise Exception("Invalid boolean value.")
        # print(inp.logout)
        if inp.logout:
            cmd = True
            if inp.logout.upper() == "TRUE":
                mgr.logout()
            else:
                raise Exception("Invalid boolean value.")
        # print(inp.wc)
        if inp.wc:
            cmd = True
            if len(inp.wc) == 1 and inp.wc[0] != "null":
                mgr.getRequestByCityName(inp.wc[0],stateCode=None,countryCode=None)
            elif len(inp.wc) == 2 and inp.wc[0] != "null":
                inp.wc[1] = inp.wc[1] if inp.wc[1] != "null" else None
                mgr.getRequestByCityName(inp.wc[0],stateCode=inp.wc[1],countryCode=None)
            elif len(inp.wc) == 3 and inp.wc[0] != "null":
                inp.wc[1] = inp.wc[1] if inp.wc[1] != "null" else None
                inp.wc[2] = inp.wc[2] if inp.wc[2] != "null" else None
                mgr.getRequestByCityName(inp.wc[0],stateCode=inp.wc[1],countryCode=inp.wc[2])
            else:
                raise Exception("Invalid input list: CityName StateCode CountryCode",inp.wc,len(inp.wc))
        # print(inp.w)
        if inp.w:
            cmd = True
            if len(inp.w) == 2:
                if inp.w[0] not in  ["null",None] and inp.w[1] not in  ["null",None]:
                    mgr.getRequestByLatLon(inp.w[0],inp.w[1])
                else:
                    raise Exception("Invalid values: lat & lon cannot be null.")
            else:
                raise Exception("Invalid input list: lat(required) lon(required)",inp.w,len(inp.w))
        if not cmd:
            print("Need Help: Use -h or --help for help.")  
    except Exception as e:
        print(e)
        print("Need Help: Use -h or --help for help.")
if __name__ == "__main__":
    main()