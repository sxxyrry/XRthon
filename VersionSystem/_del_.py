import shutil, os
import time


isRun = True

def del_file(path):
    shutil.rmtree(path)

def del___pycache__():
    if not os.path.exists('./__pycache__'): return
    del_file('./__pycache__')

# def del___pycache___loop():
#     while isRun:
#         del___pycache__()
#         # print('del __pycache__')

# _ = threading.Thread(target=del___pycache___loop)
# _.start()
