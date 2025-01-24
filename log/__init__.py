import os, pathlib, time, traceback
from typing import Literal, Any, TypedDict
from io import TextIOWrapper

folder = pathlib.Path(__file__).parent.resolve()

# _namelist = []

DEBUG = 'DEBUG'
INFO = 'INFO'
WARING = 'WARING'
ERROR = 'ERROR'
CRITICAL = 'CRITICAL'

_DEBUG = 4
_INFO = 3
_WARING = 2
_ERROR = 1
_CRITICAL = 0

_levellist: list[
                    Literal[
                            0,
                            1,
                            2,
                            3,
                            4
                            ]
                    ]\
                    = \
                    [
                        _DEBUG     ,
                        _INFO      ,
                        _WARING    ,
                        _ERROR     ,
                        _CRITICAL  ,
                    ]

_leveltable: dict[
                    Literal[
                            0,
                            1,
                            2,
                            3,
                            4,
                        ],
                    Literal[
                            'DEBUG',
                            'INFO',
                            'WARING',
                            'ERROR',
                            'CRITICAL',
                            ]
                    ]\
                    = \
                    {
                        _DEBUG     :  DEBUG,
                        _INFO      :  INFO,
                        _WARING    :  WARING,
                        _ERROR     :  ERROR,
                        _CRITICAL  :  CRITICAL,
                    }

class unexeceventClass(TypedDict):
    level: Literal['DEBUG', 'INFO', 'WARING', 'ERROR', 'CRITICAL']
    message: str
    time: str

class execeventClass(TypedDict):
    level: Literal['DEBUG', 'INFO', 'WARING', 'ERROR', 'CRITICAL']
    message: str
    time: str

class log():
    def __init__(self, name: str='root'):
        if name in _nametable.keys():
            self.__ie('nameisexists')

        _nametable[name] = self
        self.name = name

        self.level = _WARING
        self.format = '{time} - {level} - {name} : {message}'

        self.isusefile: bool = False
        self.isuseconsole: bool = True

        self.filemode = 'cf'
        self.filepath: str = ''
        self.fileobj: None | TextIOWrapper = None

        self.configtable: dict[str, Any] = {
                                            'level' : self.level,
                                            'format' : self.format,
                                            'isusefile' : self.isusefile,
                                            'filepath' : self.filepath,
                                            'filemode' : self.filemode,
                                            'isuseconsole' : self.isuseconsole,
                                            'fileobj' : self.fileobj
                                           }
    
        self.eventslist: list[execeventClass] = []
    
        self.unexeceventslist: list[unexeceventClass] = []

    def config(self, level: Literal['DEBUG', 'INFO', 'WARING', 'ERROR', 'CRITICAL']='WARING',
               format: str='XR - {time} - {level} - {name} : {message}',
                isusefile: bool=False, filepath: str | None=None,
                filemode: Literal['cf', 'w'] | None='cf', isuseconsole: bool=True):

        __a: dict[
                Literal['DEBUG', 'INFO', 'WARING', 'ERROR', 'CRITICAL'],
                Literal[0, 1, 2, 3, 4]
                ] = {j : i for i, j in _leveltable.items()}

        if not __a[level] in _levellist:
            self.__ie('levelisnotexists')

        self.level: Literal[0, 1, 2, 3, 4] = __a[level]

        if \
            not '{time}' in format or \
            not '{level}' in format or \
            not '{name}' in format or \
            not '{message}' in format\
            :
            self.__ie('invalidformat')
        
        self.format: str = format

        self.isusefile: bool = isusefile

        self.isuseconsole: bool = isuseconsole

        self.filemode: Literal['cf', 'w'] | None = filemode or 'w'

        if self.isusefile:
            if filepath is None:
                self.__ie('fileisnotexists')
            else:
                if not os.path.exists(filepath):
                    if filemode =='cf':
                        open(filepath, 'w').write('')
                    elif (filemode == 'w'):
                        self.__ie('fileisnotexists')
                    else:
                        self.__ie('invalidfilemode')

                # if self.name == 'root':
                #     __fileobj = open(filepath, 'r', encoding='UTF-8')
                #     if __fileobj.read() != '':
                #         open(filepath, 'w').write('')
                    
                #     del __fileobj

                print(filepath)

                self.fileobj: None | TextIOWrapper = open(filepath, 'a', encoding='UTF-8')

        if self.configtable == {
                                'level' : self.level,
                                'format' : self.format,
                                'isusefile' : self.isusefile,
                                'filepath' : self.filepath,
                                'filemode' : self.filemode,
                                'isuseconsole' : self.isuseconsole,
                                'fileobj' : self.fileobj
                                }:
            return self

        self.configtable.update({
                                 'level' : self.level,
                                 'format' : self.format,
                                 'isusefile' : self.isusefile,
                                 'filepath' : self.filepath,
                                 'filemode' : self.filemode,
                                 'isuseconsole' : self.isuseconsole,
                                 'fileobj' : self.fileobj
                                })

        return self

    def get_log(self, name):
        # print(self.name)
        # if self.name == 'root':
        #     _log = log(name)
        #     _log.config(
        #                 level=_leveltable[self.level],
        #                 format=self.format,
        #                 isusefile=self.isusefile,
        #                 filename=self.__filename,
        #                 filemode=self.filemode,
        #                 root_dir=self.root_dir,
        #                 isuseconsole=self.isuseconsole
        #                )
        # return _log
        # else:
        #     return log(name)
        return log(name)

    def __log(self, level: Literal[0, 1, 2, 3, 4], message: str):
        text = self.format.format(time=time.strftime('%Y-%m-%d %H:%M:%S',
                                                            time.localtime()),
                                        level=_leveltable[level],
                                        name=self.name,
                                        message=message)
        if self.isusefile:
            if not self.fileobj is None:
                self.fileobj.write(text + '\n')
            else:
                self.__ie('fileobjisnotexists')
        if self.isuseconsole:
            print(text)
        else:
            self.unexeceventslist.append({'level' : _leveltable[level], 'message' : text, 'time' : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())})

        self.eventslist.append({'level' : _leveltable[level], 'message' : text, 'time' : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())})

    def debug(self, message: str):
        if self.level >= _DEBUG:
            self.__log(_DEBUG, message)
        else:
            pass
    
    def info(self, message: str):
        if self.level >= _INFO:
            self.__log(_INFO, message)
        else:
            pass

    def warning(self, message: str):
        if self.level >= _WARING:
            self.__log(_WARING, message)
        else:
            pass
    
    def error(self, message: str):
        if self.level >= _ERROR:
            self.__log(_ERROR, message)
        else:
            pass

    def critical(self, message: str):
        if self.level >= _CRITICAL:
            self.__log(_CRITICAL, message)
        else:
            pass

    def get_exception(self, exc_info=None):
        if exc_info is None:
            exc_info = traceback.format_exc()
        else:
            exc_info = traceback.format_exception_only(*exc_info[:2])
            exc_info = ''.join(exc_info)

        self.error(f"Exception occurred: \n{exc_info}")



    def exit(self):
        if self.name == 'root':
            return
        _nametable.pop(self.name)
        del self
        return

    def __ie(self, error: str):
        table: dict[str, str] = {
                                    'nameisexists'        :  'name is exists',
                                    'errorisnotexists'    :  'error is not exists',
                                    'levelisnotexists'    :  'level is not exists',
                                    'invalidformat'       :  'format is invalid',
                                    'fileisnotexists'     :  'file is not exists',
                                    'invalidfilemode'     :  'filemode is invalid',
                                    # 'fileobjisnotexists'  :  'file object is not exists',
                                }
        if ' ' in error:
            for i in error.split(' '):
                if i in table:
                    pass
                else:
                    self.__ie('errorisnotexists')
            
            raise Exception(' '.join([table[i] for i in error.split(' ')]))

        if not error in table:
            self.__ie('errorisnotexists')
        
        raise Exception(table[error])

    def GetEventsList(self) -> list[execeventClass]:
        return self.eventslist

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exit()
        return

_nametable: dict[str, log] = {}

root_log = log('root')

# debug = root_log.debug
# info = root_log.info
# warning = root_log.warning
# error = root_log.error
# critical = root_log.critical
# get_exception = root_log.get_exception
# # basicconfig = root_log.config
# config = root_log.config
# get_log = root_log.get_log

def debug(message: str):
    return root_log.debug(message)

def info(message: str):
    return root_log.info(message)

def warning(message: str):
    return root_log.warning(message)

def error(message: str):
    return root_log.error(message)

def critical(message: str):
    return root_log.critical(message)

def get_exception(exc_info=None):
    return root_log.get_exception(exc_info)

def get_log(name: str):
    return root_log.get_log(name)

def config(level: Literal['DEBUG', 'INFO', 'WARING', 'ERROR', 'CRITICAL']='WARING',
            format: str='XR - {time} - {level} - {name} : {message}',
            isusefile: bool=False, filepath: str | None=None,
            filemode: Literal['cf', 'w'] | None='cf', isuseconsole: bool=True):
    root_log.config(level=level, format=format, isusefile=isusefile, filepath=filepath, filemode=filemode, isuseconsole=isuseconsole)

def basicconfig(level: Literal['DEBUG', 'INFO', 'WARING', 'ERROR', 'CRITICAL']='WARING',
                format: str='XR - {time} - {level} - {name} : {message}',
                isusefile: bool=False, filepath: str | None=None,
                filemode: Literal['cf', 'w'] | None='cf', isuseconsole: bool=True):
    for log in _nametable.values():
        log.config(level=level, format=format, isusefile=isusefile, filepath=filepath, filemode=filemode, isuseconsole=isuseconsole)
