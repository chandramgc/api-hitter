import git
import os
import glob
import shutil

loc = "C:/Users/chand/Documents/Workspace/vcode/temp-workspace"
locGit = "C:/Users/chand/Documents/Workspace/vcode/temp-workspace/.git"
gitUrl = "https://github.com/chandramgc/yaml-reader-private.git"


if os.name == 'nt':
    import win32api, win32con
def file_is_hidden(p):
    if os.name== 'nt':
        attribute = win32api.GetFileAttributes(p)
        return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
    else:
        return p.startswith('.') #linux-osx

files = glob.glob(loc+"/*", recursive=True)
try:
    [os.remove(f) for f in os.listdir(loc) if file_is_hidden(f)]
except OSError as e:
    print("Error: %s : %s" % (locGit, e.strerror))

for f in files:
    try:
        os.remove(f)
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))

repo = git.Repo.clone_from(gitUrl,loc)