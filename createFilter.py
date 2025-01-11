
colors = {}
mapStyle = {1:{"PlayEffect":"Purple", 
               "MinimapIcon":"0 Orange Circle", 
               "SetTextColor":"200 200 200 255",
               "SetBackgroundColor":"0 0 0 240"},
               "SetBorderColor":"229 23 23 255",
               "SetFontSize":"45"}
def getMapStyle(value):
    if value == 1:
        return "    SetTextColor 0 0 0\n\
    SetBackgroundColor 255 255 255\n\
    SetBorderColor 128 128 128\n\
    SetFontSize 50\n\
    DisableDropSound True\n\
    CustomAlertSound \"文子过滤音效\高级地图.mp3\"\n\
    MinimapIcon 0 Pink Hexagon\n\
    PlayEffect Pink\n"

def processMaps(mapFiter, mapLine):
    infos = mapLine.split("#")[:-1]
    print(infos)
    fiterInfo = 'Show\n'
    fiterInfo = fiterInfo + "    Class " + infos[1] + " #" + infos[4] + "\n"
    fiterInfo = fiterInfo + "    Class " + infos[1] + " #" + infos[4] + "\n"
    fiterInfo = fiterInfo + "    BaseType " + infos[2] + "\n"
    print(fiterInfo)
    fiterInfo = fiterInfo + getMapStyle(int(infos[3]))
    mapFiter.append(fiterInfo)

def readItems():
    with open("./items.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    fiter = []
    for line in lines:
        if line.startswith("#"):
            continue
        if line.startswith("地图"):
            processMaps(fiter, line)
    with open("./fiter.txt", 'w', encoding="utf-8") as f:
        f.writelines(fiter)

readItems()