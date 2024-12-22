from Edition_logs import Edition_logsForXRthon, Edition_logsForEditor


def GetVersionForXRthon():
    version = ''

    for _ in Edition_logsForXRthon.split('\n'):
        if _.endswith(' Version:'):
            version: str = _[:-9]
    
    return version

def GetVersionForEditor():
    version = ''

    for _ in Edition_logsForEditor.split('\n'):
        if _.endswith(' Version:'):
            version: str = _[:-9]
    
    return version
