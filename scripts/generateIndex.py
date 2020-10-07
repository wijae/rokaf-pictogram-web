import os
import json

JpgResPath = "public/res/jpg"
ResIndexPath = "public/res/index.json"

data = []

categories = os.listdir(JpgResPath)
for category in categories:
    categoryFiles = []

    files = os.listdir(JpgResPath+"/"+category)
    for f in files:
        fNo = int(f[0:2])
        fName = f[4:-4]
    
        categoryFiles.append({"no": fNo, "name": fName})

    catNo = int(category[0:2])
    catName = category[4:]

    data.append({"no": catNo, "name": catName, "files": categoryFiles})


with open(ResIndexPath, 'w', encoding='UTF-8-sig') as outfile:
    json.dump(data, outfile, indent=1, ensure_ascii = False)