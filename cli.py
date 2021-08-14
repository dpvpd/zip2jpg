import shutil

print('참고 : 파일 이름 입력시, 본 exe파일과 두 파일이 같은 폴더에 있지 않다면 절대경로를 입력하는 것이 더 나을 수 있습니다. ')
jpgName = input('불러올 jpg파일의 이름 입력 : ')
zipName = input('불러올 zip파일의 이름 입력 : ')
newfile = jpgName[:-4]+'_i'+'.jpg'

with open(zipName, 'rb') as t:
    data = t.read()

try:
    shutil.copy(jpgName, newfile)
except:
    pass

with open(newfile,'ab+') as z:
    z.write(data)