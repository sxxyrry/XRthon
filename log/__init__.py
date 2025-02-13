import os, pathlib, time, traceback
from typing import Literal, Any, TypedDict
from io import TextIOWrapper
from enum import IntEnum, StrEnum


folder = pathlib.Path(__file__).parent.resolve()

class IntLevel(IntEnum):
    DEBUG = 4
    INFO = 3
    WARING = 2
    ERROR = 1
    CRITICAL = 0

class StrLevel(StrEnum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARING = 'WARING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

IntlevelToStrLevel = {
    IntLevel.DEBUG     :  StrLevel.DEBUG,
    IntLevel.INFO      :  StrLevel.INFO,
    IntLevel.WARING    :  StrLevel.WARING,
    IntLevel.ERROR     :  StrLevel.ERROR,
    IntLevel.CRITICAL  :  StrLevel.CRITICAL,
}

StrlevelToIntLevel = {v: k for k, v in IntlevelToStrLevel.items()}

class unexeceventClass(TypedDict):
    level: StrLevel
    message: str
    time: str

class execeventClass(TypedDict):
    level: StrLevel
    message: str
    time: str

class log():
    def __init__(self, name: str='root'):
        if name in _nametable.keys():
            self.__ie('nameisexists')

        _nametable[name] = self
        self.name = name

        self.level = IntLevel.WARING
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

    def config(self, level: StrLevel | None=None,
               format: str | None=None,
                isusefile: bool | None=None, filepath: str | None=None,
                filemode: Literal['cf', 'w'] | None=None, isuseconsole: bool | None=True):

        # 'XR - {time} - {level} - {name} : {message}'

        if level is not None:
            if not level in StrlevelToIntLevel.keys():
                self.__ie('levelisnotexists')
            else:
                self.level = StrlevelToIntLevel[level]
        else:
            self.level = self.level if self.level else IntLevel.WARING
        
        if format is not None:
            if \
                not '{time}' in format or \
                not '{level}' in format or \
                not '{name}' in format or \
                not '{message}' in format\
                :
                self.__ie('invalidformat')
            else:
                self.format: str = format
        else:
            self.format: str = self.format if self.format else 'XR - {time} - {level} - {name} : {message}'
        
        if isusefile is not None:
            if not isinstance(isusefile, bool):
                self.__ie('isusefileisnotbool')
            else:
                self.isusefile = isusefile
        else:
            self.isusefile = self.isusefile if self.isusefile else False

        if isuseconsole is not None:
            if not isinstance(isuseconsole, bool):
                self.__ie('isuseconsoleisnotbool')
            else:
                self.isuseconsole = isuseconsole
        else:
            self.isuseconsole = self.isuseconsole if self.isuseconsole else True

        if filemode is not None:
            if not filemode in ['cf', 'w']:
                self.__ie('invalidfilemode')
            else:
                self.filemode = filemode
        else:
            self.filemode = self.filemode if self.filemode else 'cf'

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

    def __log(self, level: IntLevel, message: str):
        text = self.format.format(time=time.strftime('%Y-%m-%d %H:%M:%S',
                                                            time.localtime()),
                                        level=IntlevelToStrLevel[level],
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
            self.unexeceventslist.append({'level' : IntlevelToStrLevel[level], 'message' : text, 'time' : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())})

        self.eventslist.append({'level' : IntlevelToStrLevel[level], 'message' : text, 'time' : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())})

    def debug(self, message: str):
        if self.level >= IntLevel.DEBUG:
            self.__log(IntLevel.DEBUG, message)
        else:
            pass
    
    def info(self, message: str):
        if self.level >= IntLevel.INFO:
            self.__log(IntLevel.INFO, message)
        else:
            pass

    def warning(self, message: str):
        if self.level >= IntLevel.WARING:
            self.__log(IntLevel.WARING, message)
        else:
            pass
    
    def error(self, message: str):
        if self.level >= IntLevel.ERROR:
            self.__log(IntLevel.ERROR, message)
        else:
            pass

    def critical(self, message: str):
        if self.level >= IntLevel.CRITICAL:
            self.__log(IntLevel.CRITICAL, message)
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
                                    'nameisexists'           :  'name is exists',
                                    'errorisnotexists'       :  'error is not exists',
                                    'levelisnotexists'       :  'level is not exists',
                                    'invalidformat'          :  'format is invalid',
                                    'isusefileisnotbool'     :  'isusefile is not a Boolean value',
                                    'isuseconsoleisnotbool'  :  'isuseconsole is not a Boolean value',
                                    'fileisnotexists'        :  'file is not exists',
                                    'invalidfilemode'        :  'filemode is invalid',
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

def config(
    level: StrLevel | None=None,
    format: str | None=None,
    isusefile: bool | None=None, filepath: str | None=None,
    filemode: Literal['cf', 'w'] | None=None, isuseconsole: bool | None=True
):
    root_log.config(level=level, format=format, isusefile=isusefile, filepath=filepath, filemode=filemode, isuseconsole=isuseconsole)

def BasicConfig(
    level: StrLevel | None=None,
    format: str | None=None,
    isusefile: bool | None=None, filepath: str | None=None,
    filemode: Literal['cf', 'w'] | None=None, isuseconsole: bool | None=True
):
    for log in _nametable.values():
        log.config(level=level, format=format, isusefile=isusefile, filepath=filepath, filemode=filemode, isuseconsole=isuseconsole)
