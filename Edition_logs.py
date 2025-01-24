import os
from folder import folder


with open(os.path.join(folder, './TextFIles/Edition_logs/English/Edition_logsForXRthon.txt'), 'r', encoding='UTF-8') as f:
    English_Edition_logsForXRthon: str = f.read()

with open(os.path.join(folder, './TextFIles/Edition_logs/English/Edition_logsForEditor.txt'), 'r', encoding='UTF-8') as f:
    English_Edition_logsForEditor: str = f.read()
