from main import Interpreter


print('XRthon programming language')
print('version: BETA 0.0.1 _indev 2024*11*3')

interpreter = Interpreter('main', config={'ContinueRunningAfterError': True})

running = True
while running:
    try:
        command = input(' > ')

        if command in interpreter.environment.values.keys():
            print(interpreter.environment.values[command]['value'])
        else:
            interpreter.run_forlinetext(command, [command], None, 1)
    except KeyboardInterrupt as e:
        print('^C\n', end='')
        interpreter.raiser('KeyboardInterrupt', 'User pressed Ctrl+C', 1, '^C', '<String>', e) # type: ignore
    except EOFError as e:
        print('^V\n', end='')
        interpreter.raiser('EOFError', 'User pressed Ctrl+V', 1, '^V', '<String>', e)
