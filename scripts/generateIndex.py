import os
import json

JpgResPath = "src/assets/res/jpg"
ResIndexPath = "src/iconIndex.json"

data = []

categories = os.listdir(JpgResPath)
for category in categories:
    categoryFiles = []

    files = os.listdir(JpgResPath+"/"+category)
    for f in files:
        fNo = f[0:2]
        fName = f[4:-4]
        fpath = category + "/" + f[0:-4]
    
        categoryFiles.append({"id": fNo, "name": fName, "path": fpath})

    catNo = category[0:2]
    catName = category[4:]

    data.append({"id": catNo, "name": catName, "path": category, "iconPath": categoryFiles[0]["path"], "icons": categoryFiles})


with open(ResIndexPath, 'w', encoding='UTF-8-sig') as outfile:
    json.dump(data, outfile, indent=1, ensure_ascii = False)