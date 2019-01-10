import os

with open("version", "r+", encoding='utf-8') as versionfile:
    print("Reading version file...")
    verinfo = versionfile.read().split()
    versionfile.seek(0)
    print(verinfo)
    count = 0
    for i in verinfo:
        verinfo[count] = int(i)
        count = count + 1
    print("Calculating new version...")
    with open("PROGDETAILS.py", "w", encoding='utf-8') as programfile:
        if(verinfo[2] == 9):
            verinfo[2] = 0
            if(verinfo[1] == 9):
                verinfo[1] = 0
                verinfo[0] = verinfo[0] + 1
            else:
                verinfo[1] = verinfo[1] + 1
        else:
            verinfo[2] = verinfo[2] + 1
        print(verinfo)
        print("Writing...")
        versionfile.write(str(verinfo[0]) + " " + str(verinfo[1]) + " " + str(verinfo[2]))
        versionfile.truncate()
        programfile.seek(0)
        programfile.write("class Program:\n    def __init__(self):\n        self.version = \"" + str(verinfo[0]) + "." + str(verinfo[1]) + "." + str(verinfo[2]) + "\"")
        programfile.truncate()

os.system("pause")
exec(open("OREGON.py", encoding='utf-8').read())
os.system("pause")
