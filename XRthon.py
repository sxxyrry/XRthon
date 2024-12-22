from Runner import Runner, config_root
# from Edition_logs import Edition_logsForXRthon
from VersionSystem import VersionSystem
from colorama import init, Fore, Style, Back
from versions import GetVersionForXRthon
import time

init()

SleepTime = 0.5

version = GetVersionForXRthon()

time.sleep(SleepTime)

if VersionSystem.CheckVersion(version if '/NVSFT: ' not in version else version.split('/NVSFT: ')[1]):
    print(f'{Fore.GREEN}Check: Your XRthon Version format is Normal.{Style.RESET_ALL}')
else:
    print(f'{Fore.RED}Check: Your XRthon Version format is Invalid.{Style.RESET_ALL}')
    # raise SystemExit()

time.sleep(SleepTime)

print(f'{Fore.LIGHTCYAN_EX}{Style.BRIGHT}{Back.LIGHTYELLOW_EX}XRthon programming language{Style.RESET_ALL}')

time.sleep(SleepTime)

print(f'{Fore.LIGHTCYAN_EX}{Style.BRIGHT}{Back.LIGHTYELLOW_EX}version: {version}{Style.RESET_ALL}')

time.sleep(SleepTime)

print(f'{Fore.LIGHTCYAN_EX}You can use "import(Edition_logsForXRthon)" to views edition log.{Style.RESET_ALL}')

time.sleep(SleepTime)

print(f'{Fore.LIGHTCYAN_EX}You can use "help()" to views help.{Style.RESET_ALL}')

runner = Runner('main', config={'ContinueRunningAfterError': True})
config_root({'ContinueRunningAfterError': True})

running = True
while running:
    try:

        time.sleep(SleepTime)

        command = input(' > ')

        time.sleep(SleepTime)

        # if command == 'help':
        #     print('a')

        if '.' in command:
            parts = command.split('.')
            if '(' in parts[0]:
                runner.run_forlinetext(command, [command], None, 1)
            else:
                name = parts[0]
                attr_path = '.'.join(parts[1:])
                
                try:
                    # 获取环境中的对象
                    obj = runner.environment.values[name]['value']
                    
                    # 逐层获取属性或方法
                    attr = obj
                    for part in attr_path.split('.'):
                        _ = attr[part]
                        attr = _['value'] if isinstance(_, dict) else _
                    
                    # 执行属性或方法
                    # if callable(attr):
                    #     result = attr()
                    # else:
                    result = attr['value'] if isinstance(attr, dict) and 'value' in attr else attr
                    
                    print(result)
                except Exception as e:
                    runner.raiser(f'{e.__class__.__name__}', f'{e}', 1, command, '<String>', e, runner.config)
        else:
            if command in runner.environment.values.keys():
                print(runner.environment.values[command]['value'])
            else:
                runner.run_forlinetext(command, [command], None, 1)
    except KeyboardInterrupt as e:
        print('^C\n', end='')
        runner.raiser('KeyboardInterrupt', 'User pressed Ctrl+C', 1, '^C', '<String>', e) # type: ignore
    except EOFError as e:
        print('^V\n', end='')
        runner.raiser('EOFError', 'User pressed Ctrl+V', 1, '^V', '<String>', e)
