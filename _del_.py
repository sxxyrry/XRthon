# import shutil, threading, os
import shutil, os
# import time


# isRun = True

def del_file(path):
    shutil.rmtree(path)

def del___pycache__():
    if os.path.exists('./custom/__pycache__/'):
        del_file('./custom/__pycache__/')
    if os.path.exists('./log/__pycache__/'):
        del_file('./log/__pycache__/')
    if os.path.exists('./__pycache__'):
        del_file('./__pycache__')

# def del___pycache___loop():
#     while isRun:
#         del___pycache__()
#         # print('del __pycache__')

# _ = threading.Thread(target=del___pycache___loop)
# _.start()
