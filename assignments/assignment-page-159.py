import os

fpath = '.\\assignment-page-159'
files = os.listdir(fpath)
txtFiles = []
i = 0

for x in files:
    if x.endswith('.txt'):
        txtFiles.append(x)

while i < len(txtFiles):
    print("{} was modified at {}".format(txtFiles[i],os.path.getmtime(os.path.join(fpath,txtFiles[i]))))
    i += 1
