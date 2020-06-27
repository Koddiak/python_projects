import shutil, os
from datetime import *

source = './/assignment-page-229/source/'
destination = './/assignment-page-229/destination/'
files = os.listdir(source)

for i in files:
    dateModified = datetime.fromtimestamp(os.path.getmtime(source+i))
    dateCreated = datetime.fromtimestamp(os.path.getctime(source+i))
    yesterday = datetime.now() - timedelta(days=1)
    
    if dateModified > yesterday and dateCreated > yesterday:
        print('{} was moved.'.format(i))
        shutil.move(source+i,destination)
    else:
        print('{} was not moved.'.format(i))
        continue
