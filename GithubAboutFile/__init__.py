from .AddLineToFile import AddLineToFile
from .ChangeFile import ChangeFile
from .CreateDir import CreateDir
from .CreateFile import CreateFile
from .DeleteFile import DeleteFile
from .DirExists import DirExists
from .DownloadDir import DownloadDir
from .DownloadFile import DownloadFile
from .FileExists import FileExists
from .GetFileAndDirsNameList import GetFileAndDirsNameList
from .GetFileText import GetFileText
from .UploadFile import UploadFile


__all__: list[str] = [
                      'AddLineToFile',
                      'ChangeFile',
                      'CreateDir',
                      'CreateFile',
                      'DeleteFile',
                      'DirExists',
                      'DownloadDir',
                      'DownloadFile',
                      'FileExists',
                      'GetFileAndDirsNameList',
                      'GetFileText',
                      'UploadFile',
                     ]

def del_():
    import shutil, os, pathlib
    folder = pathlib.Path(__file__).parent.resolve()

    if os.path.exists(os.path.join(folder, './__pycache__')):
        shutil.rmtree(os.path.join(folder, './__pycache__'))

del_()

del del_
