
maps = {"Class":"Maps", "BaseType":"", "MapTier":"", }

class Info:
    '过滤信息'

    def __init__(self, value):
        self.__value = value
        self.__Class = ""
        self.__BaseType = ""
        self.__SetTextColor = ""
        self.__SetBackgroundColor = ""
        self.__setBorderColor = ""
        self.__SetFontSize = ""
        #DisableDropSound
        self.__Minimaplcon = ""
        self.__PlayEffect = ""
        self.__CustomAlertSound = ""
        self.setStyle()
    
    def setStyle(self):
        if self.__value == 1:
            pass
        elif self.__value == 2:
            pass
        elif self.__value == 3:
            pass
        elif self.__value == 4:
            pass
        elif self.__value == 5:
            pass 
        elif self.__value == 0:
            pass
    
    def printInfo(self):
        string = "Show\n  Class " + self.__Class
        pass

class Map:
    '地图类'

    def __init__(self):
        self.maps = []
        self.special = ["Pit of the Chimera Map", "Lair of the Hydra Map", \
                        "Maze of the Minotaur Map", "Maze of the Minotaur Map", "Harbinger Map",\
                        "Engraved Ultimatum", "Vaal Temple Map"]
        self.info = Info(-1)

    def processMaps(self):
        '四守卫地图、征服者地图、裂界守卫地图、瓦尔密殿、意境地图、传奇地图、T1456、红图、黄图、白图'
        pass

#class                 

if __name__ == "__main__":
    pass