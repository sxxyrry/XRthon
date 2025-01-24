import os
import time
import py7zr
from folder import folder


szfp = os.path.join(folder, './files/AddEnvVarOfDir.7z')
jyp = os.path.join(folder)
allfilename = [
    'AddEnvVarOfDir.deps.json',
    'AddEnvVarOfDir.dll',
    'AddEnvVarOfDir.exe',
    'AddEnvVarOfDir.pdb',
    'AddEnvVarOfDir.runtimeconfig.json',
]
py7zr.unpack_7zarchive(szfp, jyp)

os.startfile(os.path.join(folder, './AddEnvVarOfDir.exe'))

time.sleep(1)

for i in allfilename:
    os.remove(os.path.join(folder, i))
