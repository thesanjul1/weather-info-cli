from parserInputManager import Manager

def main():
    try:
        mgr = Manager()
        mgr.respUsername()
        if mgr.isCreate():
            mgr.respCreate()
        if mgr.isUpdate():
            mgr.respUpdate()
        if mgr.isDelete():
            mgr.respDelete()
        if mgr.isAll():
            mgr.respAll()
        if mgr.isLogout():
            mgr.respLogout()
        if mgr.isWeatherByCity():
            mgr.respWeatherByCity()
        if mgr.isWeatherByLatLon():
            mgr.respWeatherByLatLon()
        if not mgr.isCommand():
            print("Need Help: Use -h or --help for help.")  
    except Exception as e:
        print(e)
        print("Need Help: Use -h or --help for help.")

if __name__ == "__main__":
    main()
