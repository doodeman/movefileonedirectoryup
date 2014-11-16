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

filename = sys.argv[1]
try:
    path = os.path.dirname(os.path.abspath(__file__)) + "\\" + filename
except NameError: 
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    
if IsAtRoot(path):
    sys.exit(0)
else:
    newpath = OneFolderUp(path)
    os.rename(path, newpath)
