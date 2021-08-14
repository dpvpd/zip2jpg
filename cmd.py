import shutil, sys

jpgName = sys.argv[1]
zipName = sys.argv[2]
newfile = jpgName[:-4]+'_i'+'.jpg'

with open(zipName, 'rb') as t:
    data = t.read()

try:
    shutil.copy(jpgName, newfile)
except:
    pass

with open(newfile,'ab+') as z:
    z.write(data)