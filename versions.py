from Edition_logs import English_Edition_logsForXRthon, English_Edition_logsForEditor


def GetVersionForXRthon():
    version = ''

    for _ in English_Edition_logsForXRthon.split('\n'):
        if _.endswith(' Version:'):
            version: str = _[:-9]
        elif _.endswith(' Version:\r'):
            version: str = _[:-10]
    
    return version

def GetVersionForEditor():
    version = ''

    for _ in English_Edition_logsForEditor.split('\n'):
        if _.endswith(' Version:'):
            version: str = _[:-9]
        elif _.endswith(' Version:\r'):
            version: str = _[:-10]
    
    return version

def GetVersion(EditionLogs: str) -> str:
    version = ''

    for _ in EditionLogs.split('\n'):
        if _.endswith(' Version:'):
            version: str = _[:-9]
        elif _.endswith(' Version:\r'):
            version: str = _[:-10]
    
    return version
