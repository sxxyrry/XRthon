import os
from folder import folder


with open(os.path.join(folder, './Edition_logs/Edition_logsForXRthon.txt'), 'r', encoding='UTF-8') as f:
    Edition_logsForXRthon: str = f.read()

with open(os.path.join(folder, './Edition_logs/Edition_logsForEditor.txt'), 'r', encoding='UTF-8') as f:
    Edition_logsForEditor: str = f.read()
