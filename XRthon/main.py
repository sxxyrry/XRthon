import os
from folder import folder
from types import NoneType
from typing import Any, TypedDict


# 定义关键字、运算符和标点符号
keys = [
    'def_class',
    'def_function',
    'END',
    'if',
    'else',
    'elif',
    'for',
    'while',
    'in',
    'and',
    'or',
    'not',
    'True',
    'False',
    'None',
    'return',
    'pass',
    'continue',
    'break',
    'lambda',
    'try',
    'except',
    'finally',
    'raise',
    'assert',
    'global',
    'nonlocal',
    'del',
    'import',
    'from',
    'as',
    'with',
    'yield',
    'async',
    'await',
]

operators = [
    '==', '!=', '>', '<', '>=', '<=',
    '+', '-', '*', '/', '//', '%', '**',
    '=', '+=', '-=', '*=', '/=', '//=', '%=', '**=',
    '&=', '|=', '^=', '<<=', '>>=',
]

punctuation = [
    '(', ')', '[', ']', '{', '}', ',', ':', ';', '.',
]

ErrorTable = [
    ''
]

BuiltinsFunctoins = [
    'print',
    'input',
    'import',
    'quit',
    # 'len',
    # 'type',
    # 'int',
    # 'float',
    # 'str',
    # 'bool',
    # 'list',
    # 'dict',
    # 'tuple',
    # 'set',
    # 'range',
    # 'min',
    # 'max',
    # 'sum',
    # 'eval',
    # 'exec',
    # 'open',
]

BuiltinsPackages = [
    'os',
    'sys',
    # 'math',
    # 'random',
    # 'time',
    # 'datetime',
    # 'json',
    # 'pickle',
    # 're',
    # 'requests',
    # 'tkinter',
]

PackagesFolderPath = os.path.join(folder, 'packages')

# class XRTypes():
#     def __init__(self, type: str, value: str):
#         self.type = type
#         self.value = value

class configType(TypedDict):
    ContinueRunningAfterError: bool

class Raiser():
    def __init__(
                 self,
                 type_: str,
                 message: str,
                 line: int,
                 text: str,
                 path: str,
                 pythonserror: Exception | None = None,
                 config: configType={'ContinueRunningAfterError': False}
                ):
        if type_ == 'SystemExit':
            raise SystemExit()
        print(f'Traceback (most recent call last):')
        print(f'    File "{path}", line {line}')
        print(f'        {text}')
        print(f'        {len(text) * '^'}')
        print(f'{type_} : {message}')
        if pythonserror is not None:
            print(f'Python Level Errors:')
            print(f'{pythonserror.__class__.__name__} : {pythonserror}')
        if config['ContinueRunningAfterError'] == False:
            raise SystemExit()
        # elif config['ContinueRunningAfterError'] == 'warn':
        #     print('Warning: The program will continue running after an error.')
        # elif config['ContinueRunningAfterError'] == 'ignore':
        #     print('Warning: The program will ignore the error.')
        elif config['ContinueRunningAfterError'] == True:
            pass

# class valuesType(TypedDict):


class Environment():
    def __init__(self, name: str, values: dict[str, dict[str, dict]]):
        # self.values = values
        # self.keys = keys
        # self.operators = operators
        # self.punctuation = punctuation
        # self.BuiltinsFunctoins = BuiltinsFunctoins
        self.name = name
        self.values = values
        # self.
        pass

    def set_values(self, values: dict):
        self.values.update(values)

    def __str__(self):
        return f'Environment: {self.name}, Values: {self.values}'

Environments: dict[str, Environment] = {}

FunctionEnvironments: dict[str, Environment] = {}

class Object(object):
    def __init__(self, value: object):
        self.value = value
    
    def __add__(self, other):
        return Object(self.value + other.value)

    def __mul__(self, other):
        return Object(self.value * other.value)
    
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} [{self.value}]>'

class Str(Object):
    def __init__(self, value: object):
        self.value = str(value)
    
    def __add__(self, other):
        return Str(self.value + other.value)

    def __mul__(self, other):
        return Str(self.value * other.value)
    
    def __repr__(self) -> str:
        return f'<Object.{self.__class__.__name__} [\'{self.value}\']>'

class Int(Object):
    def __init__(self, value: object, number, linetext, path):
        try:
            self.value = int(value) # type: ignore
        except Exception as e:
            Raiser(
                   'ValueError',
                   f'Cannot convert {value} to int',
                   number,
                   linetext,
                   path if not path is None else '<String>',
                   e
                  )
        
        self.number = number
        self.linetext = linetext
        self.path = path
    
    def __add__(self, other):
        return Int(self.value + other.value, self.number, self.linetext, self.path)

    def __mul__(self, other):
        return Int(self.value * other.value, self.number, self.linetext, self.path)
    
    def __repr__(self) -> str:
        return f'<Object{self.__class__.__name__} [{self.value}]>'

class Function(Object):
    def __init__(self, name: str, args: list[str], argsname: list[str], kwargs: dict[str, str], body: list[str], number, linetext, path):
        self.name = name
        self.args = args
        self.argsname = argsname
        self.kwargs = kwargs
        self.body = body
        self.number = number
        self.linetext = linetext
        self.path = path
        self.interpreter = FunctionInterpreter(self.name, self.args, self.argsname, self.kwargs, self.body)
    
    def __call__(self, *args):
        return self.run(args)
    
    def run(self, args):
        # return 'Function Called'
    
        self.interpreter.run

    def __repr__(self) -> str:
        return f'<Object{self.__class__.__name__} [{self.name}]>'

class Float(Object):
    def __init__(self, value: object, number, linetext, path):
        try:
            self.value = float(value) # type: ignore
        except Exception as e:
            Raiser(
                   'ValueError',
                   f'Cannot convert {value} to float',
                   number,
                   linetext,
                   path if not path is None else '<String>',
                   e
                  )
        
        self.number = number
        self.linetext = linetext
        self.path = path
    
    def __add__(self, other):
        return Float(self.value + other.value, self.number, self.linetext, self.path)

    def __mul__(self, other):
        return Float(self.value * other.value, self.number, self.linetext, self.path)
    
    def __repr__(self) -> str:
        return f'<Object{self.__class__.__name__} [{self.value}]>'

class NoneType_(Object):
    def __init__(self, v: None):
        self.v = None
    
    def __repr__(self) -> str:
        return f'<Object{self.__class__.__name__} [{self.value}]>'

class FunctionInterpreter():
    def __init__(self, EnvironmentName: str, args: list[str], argsname: list[str], kwargs: dict[str, str], body: list[str]):
        self.interpreter = Interpreter(EnvironmentName)
        for i in range(len(args)):
            self.interpreter.environment.set_values({argsname[i]: args[i]})
        
        for key, value in kwargs.items():
            self.interpreter.environment.set_values({key: value})

        self.body = body
        self.EnvironmentName = EnvironmentName
        FunctionEnvironments.update({EnvironmentName : self.interpreter.environment})
    
    def run(self):
        for line in self.body:
            self.interpreter.run_forlinetext(line, self.body)

class Interpreter():
    def __init__(self, EnvironmentName: str, *, config: configType={'ContinueRunningAfterError': False}):
        self.raiser = Raiser
        self.environment = Environment(EnvironmentName, {})
        self.EnvironmentName = EnvironmentName
        Environments.update({EnvironmentName : self.environment})
        self.config = config

    def run_forfilepath(self, filepath: str):
        with open(os.path.join(filepath), 'r') as f:
            texts = f.read()
        
        self.run_fortexts(texts, filepath)

    def run_fortexts(self, texts: str, path: str | None = None):
        number = 0
        alltextlist = texts.split('\n')
        for line in alltextlist:
            number += 1

            if line == '':
                continue
            
            self.run_forlinetext(line, alltextlist, path, number)

    def run_forlinetext(self, linetext: str, alltextlist: list[str], path: str | None = None, number: int = 1):
        try:
            linetext = '#'.join(linetext.split('#')[0:-1]) if '#' in linetext else linetext
            
            if 'END' in linetext:
                return
                
            # elif 'def_function' in linetext:
            #     name: str = linetext.split('(')[0][11:][-1]
            #     args: list[str] = linetext.split('(')[1].split(')')[0].split(',')
            #     function_body: str = ''
            #     while 1:
            #         number += 1
            #         line = alltextlist[number]
            #         if line == 'END python_code':
            #             break
            #         function_body += line + '\n'
                
            #     self.environment.set_values({name: {'args' : args, 'function_body' : function_body, 'len' : len(function_body)}})

            elif '=' in linetext:
                IsPrivateVariable = False
                list_ = linetext.split('=')
                name = list_[0]
                name = name if name[0] != ' ' else name[1:]
                v = '='.join(list_[1:])
                v = v if v[0] != ' ' else v[1:]
                type_ = None
                
                if name.split('(')[0] in BuiltinsFunctoins:
                    _1: tuple[int | str | Any | None, Int | Str | NoneType_, bool] = Functions.FunctionsLogic(self, v, number, path if not path is None else '<String>', name) # type: ignore

                    v = _1[0]
                    type_ = _1[1]
                    IsPrivateVariable = _1[2]

                _2: tuple[float | dict[Any, Any] | str | object, Float | Any | Str | Int | Object | None] = Variable.VariableLogic(self, v, number, linetext, path if not path is None else '<String>') # type: ignore

                v = _2[0]
                type_ = _2[1]
                # IsPrivateVariable = _[2]

                self.environment.set_values({name : {'value' : v, 'len' : len(str(v)), 'IsPrivateVariable' : IsPrivateVariable, 'type' : type_}})

            elif '(' in linetext:
                Functions.FunctionsLogic(self, linetext, number, path if not path is None else '<String>')

            Environments[self.EnvironmentName] = self.environment
        except KeyboardInterrupt as e:
            print('^C\n', end='')
            self.raiser('KeyboardInterrupt', 'User pressed Ctrl+C', 1, '^C', path if not path is None else '<String>', e) # type: ignore
        except EOFError as e:
            self.raiser('EOFError', 'User pressed Ctrl+V', 1, '^V', path if not path is None else '<String>', e)

class Functions():
    @staticmethod
    def FunctionsLogic(clsobj: Interpreter, linetext: str, number: int, path: str, name: str | None=None):
        if linetext.split('(')[0].startswith(BuiltinsFunctoins[0]):
            p = linetext[6:][:-1]
            
            try:
                _ = Variable.VariableLogic(clsobj, p, number, linetext, path if not path is None else '<String>')
                p = _[0]
            except Exception as e:
                if not p == '':
                    clsobj.raiser('NameError', 'Name is not defined', number, linetext, path if not path is None else '<String>', e, clsobj.config)
                    return

            v = str(print(p))
        
        elif linetext.split('(')[0].startswith(BuiltinsFunctoins[1]):
            p = linetext[6:][:-1]

            try:
                _ = Variable.VariableLogic(clsobj, p, number, linetext, path if not path is None else '<String>')
                p = _[0]
            except Exception as e:
                if not p == '':
                    clsobj.raiser('NameError', 'Name is not defined', number, linetext, path if not path is None else '<String>', e, clsobj.config)
                    return

            v = input(p)

        elif linetext.split('(')[0].startswith(BuiltinsFunctoins[2]):
            p = linetext[7:][:-1]

            if p in Environments.keys():
                clsobj.environment.set_values({p : {'value' : Environments[p].values}})
                print(clsobj.environment.values)
            else:
                if p in os.listdir(PackagesFolderPath):
                    path = f'{PackagesFolderPath}/{p}'
                
                    interpreter = Interpreter(p)
                
                    for fn in os.listdir(path):
                        if fn.endswith('.XRthon'):
                            fp = f'{path}/{fn}'
                            
                            interpreter.run_forfilepath(fp)

                    clsobj.environment.set_values({p : {'value' : interpreter.environment.values}})

                elif f'{p}.XRthon' in os.listdir(PackagesFolderPath):
                    interpreter = Interpreter(p)
                    
                    path = f'{PackagesFolderPath}/{p}.XRthon'

                    interpreter.run_forfilepath(path)
                
                    clsobj.environment.set_values({p : {'value' : interpreter.environment.values}})
                
                elif p in BuiltinsPackages:
                    if p == 'os':
                        clsobj.environment.set_values({'os' : {'value' : {i : j for i, j in os.__dict__.items()}}})
                    elif p == 'math':
                        import math
                        clsobj.environment.set_values({'math' : {'value' : {i : j for i, j in math.__dict__.items()}}})
                    else:
                        pass
                    
                
                else:
                    clsobj.raiser('NameError', 'Name is not defined', number, linetext, path if not path is None else '<String>', config=clsobj.config)
                    return

            v = 'None'

        elif linetext.split('(')[0].startswith(BuiltinsFunctoins[3]):
            # name = linetext[4:][:-1]

            clsobj.raiser('SystemExit', '', number, linetext, path if not path is None else '<String>', config=clsobj.config)

            pass

        elif linetext.split('(')[0].startswith(keys[1]):
            name = linetext[13:][:-1]
            v = 'None'

        else:
            v = 'None'

        v = f'\'{v}\''.replace('\\', '\\\\')

        type_ = Str(v)

        try:
            v = eval(v)
        except Exception as e:
            if type(e) == NameError:
                clsobj.raiser(
                            'NameError',
                            f'The name ({v}) is not defined',
                            number,
                            linetext,
                            path if not path is None else '<String>',
                            e,
                            clsobj.config
                        )
                return
            else:
                clsobj.raiser(
                            'SyntaxError',
                            'Invalid syntax',
                            number,
                            linetext, path if not path is None else '<String>',
                            e,
                            clsobj.config
                        )
                return

        try:
            try:
                if type(v) == str:
                    if '\'' in v:
                        exec(f'{name} = "{v}"')
                    if '\"' in v:
                        exec(f'{name} = \'{v}\'')
                else:
                    exec(f'{name} = {v}')
                if name in keys:
                    clsobj.raiser(
                                'SyntaxError',
                                'Invalid syntax',
                                number,
                                linetext,
                                path if not path is None else '<String>',
                                SyntaxError('invalid syntax'),
                                clsobj.config
                            )
                    return
            except Exception as e:
                clsobj.raiser(
                            'SyntaxError',
                            'Invalid syntax',
                            number,
                            linetext,
                            path if not path is None else '<String>',
                            e,
                            clsobj.config
                        )
                return

            IsPrivateVariable = False

            if name.startswith('__'): # type: ignore
                IsPrivateVariable = True

            if type(v) == int:
                type_ = Int(v, number, linetext, path)
            elif type(v) == str:
                type_ = Str(v)
            elif type(v) == NoneType:
                type_ = NoneType_(v)

            return v, type_, IsPrivateVariable
        except Exception as e:
            return

class Variable():
    @staticmethod
    def VariableLogic(clsobj: Interpreter, value: object, number: int, linetext: str, path: str):
        type_ = None
        
        value = str(value)
        if '.' in value:
            try:
                value = float(value)
                type_ = Float(value, number, linetext, path)
            except:
                f = str(value).split('.')[0]
                s = str(value).split('.')[1]
                
                if f in clsobj.environment.values.keys():
                        if s in clsobj.environment.values[f].keys():
                            value = clsobj.environment.values[f][s]
                            type_ = clsobj.environment.values[f][s]['type']
                
        else:
            if (value.startswith('"') and value.endswith('"')) \
               or (value.startswith('\'') and value.endswith('\'')):
                value = value[1:-1]
                type_ = Str(value)

            else:
                value = eval(value) if value not in clsobj.environment.values.keys() else clsobj.environment.values[value]['value']

                t = type(value)

                type_ = Int(value, number, linetext, path) if t == int \
                             else Float(value, number, linetext, path) if t == float \
                             else Str(value) if t == str \
                             else Object(value)
        
        return value, type_
                
if __name__ == '__main__':
    code = '''\
    a = input('Enter a number: ')
    # _class = '857twf'
    _A = 'ewviup' # auoikcw
    print('a')
    print(_A)
    __a = 1203
    '''

    code2 = '''
    import(a)
    print(a.__a)
    '''

    interpreter_a = Interpreter('a')

    interpreter_a.run_fortexts(code)

    # print(interpreter_a.environment.values)

    interpreter_b = Interpreter('b')

    interpreter_b.run_fortexts(code2)

    # print(interpreter_b.environment.values)
