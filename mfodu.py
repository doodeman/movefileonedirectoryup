import sys
import os

def IsAtRoot(path):
    d = dict.fromkeys(path, 0)
    for c in path:
        d[c] += 1
    if d['\\'] == 1:
        return True
    else:
        return False

def OneFolderUp(path):
    split = path.split('\\')
    split.pop(-2)
    return '\\'.join(split)

path = sys.argv[1]
if IsAtRoot(path):
    sys.exit(0)
else:
    newpath = OneFolderUp(path)
    os.rename(path, OneFolderUp(path))
