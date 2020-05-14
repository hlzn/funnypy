import os
import shutil
from os import listdir
from os.path import isfile, join

mypath = "C:\\Dev\\py\\filespoc"
f = []
folderNum = 1
fileNumber = 0
every = 25
fotosSubFolder = "imagesNo"
currentFolder = fotosSubFolder + str(folderNum)

newFolder = os.path.join(mypath, fotosSubFolder + str(folderNum))
os.mkdir(newFolder)
currentFolder = newFolder
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in onlyfiles:
    fileNumber = fileNumber + 1
    if (fileNumber >= every):
        fileNumber = 1
        folderNum = folderNum + 1
        newFolder = os.path.join(mypath, fotosSubFolder + str(folderNum))
        os.mkdir(newFolder)
        currentFolder = newFolder
    shutil.move(mypath + "\\" + file, currentFolder + "\\" + file)
    