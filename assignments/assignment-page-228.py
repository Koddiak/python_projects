import shutil
import os

source = './/assignment-page-228/Folder A/'

destination = './/assignment-page-228/Folder B/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i,destination)
