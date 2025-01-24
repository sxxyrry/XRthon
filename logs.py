import log


Check_log = log.log('Check')

Plugins_log = log.log('Plugins')

Runner_log = log.log('Runner')

Warning_log = log.log('Warning')

log.basicconfig(level=log.DEBUG, format='{time} - {level} - {name} : {message}')