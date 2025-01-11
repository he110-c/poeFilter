
colors = {}
textColor = {"红色":"200 200 200 255"}
mapStyle = {1:{"PlayEffect":"Purple", 
               "MinimapIcon":"0 Orange Circle", 
               "SetTextColor":"200 200 200 255",
               "SetBackgroundColor":"0 0 0 240"},
               "SetBorderColor":"229 23 23 255",
               "SetFontSize":"45"}
def commonInfo():
    return "    SetFontSize 50\n    DisableDropSound True\n"

def getStyle(value):
    if value == 1:
        return "    SetTextColor 0 0 0\n\
    SetBackgroundColor 255 255 255\n\
    SetBorderColor 128 128 128\n\
    CustomAlertSound \"文子过滤音效\高级地图.mp3\"\n\
    MinimapIcon 0 Pink Hexagon\n\
    PlayEffect Pink\n"

def processMaps(filter, mapLine):
    infos = mapLine.split("#")[:-1]
    filterInfo = 'Show\n'
    filterInfo = filterInfo + "    Class " + infos[1] + " #" + infos[4] + "\n"
    filterInfo = filterInfo + "    Class " + infos[1] + " #" + infos[4] + "\n"
    filterInfo = filterInfo + "    BaseType " + infos[2] + "\n"
    filterInfo = filterInfo + getStyle(int(infos[3]))
    filter.append(filterInfo)

def processCurrency(filter, curLine):
    pass

def processGems(filter):
    pass

def processJewel(filter):
    pass

def processFlasks(filter):
    pass

def processEquipment(filter):
    pass

def processOther(filter):
    pass

def readItems():
    with open("./items.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    allFilter = []
    for line in lines:
        if line.startswith("#"):
            continue
        if line.startswith("地图"):
            processMaps(allFilter, line)
        if line.startswith("通货"):
            processCurrency(allFilter, line)
    processFlasks(allFilter)
    processGems(allFilter)
    processJewel(allFilter)
    processEquipment(allFilter)
    processOther(allFilter)
    with open("./fiter.filter", 'w', encoding="utf-8") as f:
        f.writelines(allFilter)

readItems()
