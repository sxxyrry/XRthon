import sys, time
from Runner import Runner, config_root
# from Edition_logs import Edition_logsForXRthon
from VersionSystem import VersionSystem
from colorama import init, Fore, Style, Back
from versions import GetVersionForXRthon
from _del_ import del___pycache__
from logs import Check_log


init()

def main():
    SleepTime = 0.5

    version = GetVersionForXRthon()

    time.sleep(SleepTime)

    if VersionSystem.CheckVersion(version if '/NVSFT: ' not in version else version.split('/NVSFT: ')[1]):
        Check_log.info(f'{Fore.GREEN}Check: Your XRthon Version format is Normal.{Style.RESET_ALL}')
    else:
        Check_log.warning(f'{Fore.RED}Check: Your XRthon Version format is Invalid.{Style.RESET_ALL}')
        raise SystemExit()

    time.sleep(SleepTime)

    print(f'{Fore.LIGHTCYAN_EX}{Style.BRIGHT}{Back.LIGHTYELLOW_EX}XRthon programming language{Style.RESET_ALL}')

    time.sleep(SleepTime)

    print(f'{Fore.LIGHTCYAN_EX}{Style.BRIGHT}{Back.LIGHTYELLOW_EX}version: {version}{Style.RESET_ALL}')

    time.sleep(SleepTime)

    print(f'{Fore.LIGHTCYAN_EX}You can use "import(English_Edition_logsForXRthon)" to views edition log.{Style.RESET_ALL}')

    time.sleep(SleepTime)

    print(f'{Fore.LIGHTCYAN_EX}You can use "import(Chinese_Edition_logsForXRthon)" to views edition log (Chinese version).{Style.RESET_ALL}')

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
                        obj = runner.environment.values[name]['value'] # type: ignore
                        
                        # 逐层获取属性或方法
                        attr = obj # type: ignore
                        for part in attr_path.split('.'):
                            _ = attr[part] # type: ignore
                            attr = _['value'] if isinstance(_, dict) else _ # type: ignore
                        
                        # 执行属性或方法
                        # if callable(attr):
                        #     result = attr()
                        # else:
                        result = attr['value'] if isinstance(attr, dict) and 'value' in attr else attr # type: ignore
                        
                        print(result) # type: ignore
                    except Exception as e:
                        runner.raiser(f'{e.__class__.__name__}', f'{e}', 1, command, '<String>', e, runner.config)
            elif command == 'help()':
                text = '''\
Use "print()" to output text.
"" is a string.
'' is a string.
1 is a number.
Use "input()" to get input.
Use "name = value" to set a variable.
Use "name = input()" to get input.
Use "import()" to import a module.
Use "quit()" to end the run of your program.
Use "
def_func name{args}:
    # Code
END def_func name{args}:
" to create a function named 'name' and has arguments 'args'.
Use "name(args)" to run a function named 'name' and has arguments 'args'.
Use "
python {args}:
    # Python Code
END python {args}:
" to create and run a python code, and has arguments 'args' (Tips: The 'args' parameter is defined earlier).
Use "
if {1}:
    # Code
END if {1}:
" to create a if statement (1 is an expression that can be replaced with another expression).
\
'''
                print(text)
            else:
                if command in runner.environment.values.keys(): # type: ignore
                    print(runner.environment.values[command]['value']) # type: ignore
                else:
                    runner.run_forlinetext(command, [command], None, 1)
        except KeyboardInterrupt as e:
            print('^C\n', end='')
            runner.raiser('KeyboardInterrupt', 'User pressed Ctrl+C', 1, '^C', '<String>', e) # type: ignore
        except EOFError as e:
            print('^V\n', end='')
            runner.raiser('EOFError', 'User pressed Ctrl+V', 1, '^V', '<String>', e)

    del___pycache__()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2:
        path = sys.argv[1]
        runner = Runner(path)
        try:
            runner.run_forfilepath(path)
        finally:
            input('---------------------\nEnd Run File. Press Enter to exit\n')
    else:
        raise Exception('Invalid arguments')
