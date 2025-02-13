import os
from folder import folder
from types import NoneType
from typing import Any, TypedDict
from versions import GetVersionForXRthon
from Edition_logs import Chinese_Edition_logsForXRthon, English_Edition_logsForXRthon
from _del_ import del___pycache__
from config import Config


config = Config()

KernelName = 'XRXTR'

version = GetVersionForXRthon()

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

PackagesFolderPath = os.path.join(folder, './packages')

NowImport = []

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
            del___pycache__()
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
        self.iE = []
        # self.
        pass

    def set_values(self, values: dict):
        self.values.update(values)

    def AddImportsEnvironment(self, name: str):
        self.iE.append(name)

    def getImportsEnvironment(self):
        return self.iE
    
    def __getitem__(self, item):
        return self.values[item]

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

class Nonetype(Object):
    def __init__(self, v: None):
        self.v: None = v
    
    def __repr__(self) -> str:
        return f'<Object{self.__class__.__name__} [{self.value}]>'

def GetType(value: object) -> str: # type: ignore
    pass

class Function():
    def __init__(self, name: str, args: list[str], body: list[str], isBuiltins: bool, number: int, linetext: str):
        self.name = name
        self.args = args
        self.body = body
        self.number = number
        self.isBuiltins = isBuiltins
        # self.Returns = None

        self.env = Environment(name, {})
        self.raiser = Raiser
    
    def run(self, args: list[object]) -> object:
        if len(args) != len(self.args):
            self.raiser(
                'ValueError',
                f'Function {self.name} requires {len(self.args)} arguments, but {len(args)} arguments were given',
                self.number,
                self.body, # type: ignore
                self.name
            )
        
        globals_ = {
            self.args[i]: {
                'value' :  args[i],
                'type'  :  type(args[i]).__name__,
                'len'   :  len(str(args[i])),
            } for i in range(len(self.args))
        }

        if self.isBuiltins == True:
            exec(f'{self.body[0]}', globals=globals_)
        else:
            runner = Runner(self.name, function=True)
            self.env.set_values(globals_)
            runner.environment = self.env
            runner.raiser = self.raiser
            texts = '\n'.join(self.body)
            runner.run_fortexts(texts, None)
    
    def __repr__(self) -> str:
        return f'<Function {self.name}-{self.args}-isBuiltins={self.isBuiltins}>'

class Runner():
    def __init__(self, EnvironmentName: str, *, config: configType={'ContinueRunningAfterError': False}, function: bool=False):
        self.raiser = Raiser
        self.environment = Environment(EnvironmentName, {})
        self.EnvironmentName = EnvironmentName
        self.environment.set_values(
            {
                'Kernel' : {
                    'value' : {
                        'Name' : KernelName,
                        'Version' : version
                    },
                    # 'type' : {

                    # }
                },
            }
        )
        if not function:
            Environments.update({EnvironmentName : self.environment})
        self.config = config
        # self.from_ = from_

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
                name = name if name[-1] != ' ' else name[:-1]
                v = '='.join(list_[1:])
                v = v if v[0] != ' ' else v[1:]
                type_ = None
                
                if name.split('(')[0] in BuiltinsFunctoins:
                    _1: tuple[int | str | Any | None, Int | Str | Nonetype, bool] = Functions.FunctionsLogic(self, v, number, path if not path is None else '<String>', name) # type: ignore

                    v = _1[0]
                    type_ = _1[1]
                    IsPrivateVariable = _1[2]

                # if 
                # try:
                #     v = eval(v)
                # except Exception as e:
                #     root.raiser('SyntaxError', 'Syntax Error', number, linetext, path if not path is None else '<String>', e, root.config)
                #     return

                try:
                    exec(f'{name} = \'\'')
                except Exception as e:
                    root.raiser('SyntaxError', 'Syntax Error', number, linetext, path if not path is None else '<String>', e, root.config)
                    return

                _2: tuple[float | dict[Any, Any] | str | object, Float | Any | Str | Int | Object | None] = Variable.VariableLogic(self, v, number, linetext, path if not path is None else '<String>') # type: ignore

                v = _2[0]
                type_ = _2[1]
                # IsPrivateVariable = _[2]

                self.environment.set_values({name : {'value' : v, 'len' : len(str(v)), 'IsPrivateVariable' : IsPrivateVariable, 'type' : type_}})

            elif '(' in linetext:
                Functions.FunctionsLogic(self, linetext, number, path if not path is None else '<String>')

            else:
                Keys.KeysLogic(self, linetext, number, path if not path is None else '<String>', alltextlist)

            Environments[self.EnvironmentName] = self.environment
        except KeyboardInterrupt as e:
            print('^C\n', end='')
            root.raiser('KeyboardInterrupt', 'User pressed Ctrl+C', 1, '^C', path if not path is None else '<String>', e) # type: ignore
        except EOFError as e:
            root.raiser('EOFError', 'User pressed Ctrl+V', 1, '^V', path if not path is None else '<String>', e)

class Keys():
    @staticmethod
    def KeysLogic(clsobj: Runner, linetext: str, number: int, path: str, alltexts: list[str], name: str | None=None):
        if linetext.startswith('def_func'):
            name = linetext.split('{')[0][9:]
            args = linetext.split('{')[1][0:-2].replace(' ', '').split(',')

            body = []
            try:
                exec(f'def {name}({','.join(args)}):pass')
            except Exception as e:
                clsobj.raiser('SyntaxError', 'Syntax Error', number, linetext, path if not path is None else '<String>', e, clsobj.config)
        
            i = number

            while 1:
                lt = alltexts[i]

                if lt.startswith('END'):
                    if lt == f'END {linetext}':
                        break

                body.append(lt[4:])

                i += 1
            
            clsobj.environment.set_values(
                {
                    name : 
                    {
                        'value': 
                            Function(
                                name, args, body, False, number, linetext
                            ),
                        'len' : len(body),
                        'type' : 'function'
                    }
                }
            )

        elif linetext.startswith('python'):
            args_: list[str] = linetext.split('{')[1][:-2].replace(' ', '').split(',')
            if args_ == ['']:
                args_ = []
            
            args = {}

            for arg in args_:
                if arg in clsobj.environment.values:
                    args.update({arg : clsobj.environment.values[arg]['value']})
                else:
                    clsobj.raiser('NameError', 'Name Error', number, linetext, path if not path is None else '<String>', config=clsobj.config)

            body = []
            try:
                exec(f'def test({','.join(args)}):pass')
            except Exception as e:
                clsobj.raiser('SyntaxError', 'Syntax Error', number, linetext, path if not path is None else '<String>', e, clsobj.config)
            
            i = number

            while 1:
                lt = alltexts[i]

                if lt.startswith('END'):
                    if lt == f'END {linetext}':
                        break

                body.append(lt[4:])

                i += 1
            
            try:
                exec('\n'.join(body), args)
            except Exception as e:
                clsobj.raiser(e.__class__.__name__, str(e), number, linetext, path if not path is None else '<String>', e, clsobj.config)

class Functions():
    @staticmethod
    def FunctionsLogic(clsobj: Runner, linetext: str, number: int, path: str, name: str | None=None):
        if linetext.split('(')[0].startswith('print'):
            p = linetext[6:][:-1]
            
            try:
                _ = Variable.VariableLogic(clsobj, p, number, linetext, path if not path is None else '<String>')
                p = _[0]
            except Exception as e:
                if not p == '':
                    root.raiser('NameError', 'Name is not defined', number, linetext, path if not path is None else '<String>', e, root.config)
                    return

            print(p)
            v = None
        
        elif linetext.split('(')[0].startswith('input'):
            p = linetext[6:][:-1]

            try:
                _ = Variable.VariableLogic(clsobj, p, number, linetext, path if not path is None else '<String>')
                p = _[0]
            except Exception as e:
                if not p == '':
                    root.raiser('NameError', 'Name is not defined', number, linetext, path if not path is None else '<String>', e, root.config)
                    return

            v = input(p)

        elif linetext.split('(')[0].startswith('import'):
            p = linetext[7:][:-1]

            if p == 'English_Edition_logsForXRthon':
                print(English_Edition_logsForXRthon)

            elif p == 'Chinese_Edition_logsForXRthon':
                print(Chinese_Edition_logsForXRthon)

            elif p in os.listdir(PackagesFolderPath):
                if p in NowImport:
                    root.raiser('LoopImportError', 'Package was loop import', number, linetext, path if not path is None else '<String>', None, root.config)
                
                path = f'{PackagesFolderPath}/{p}' # /{p}
            
                runner = Runner(p)
            
                NowImport.append(p)

                if not os.path.isfile(path):
                    for fn in os.listdir(path):
                        if fn.endswith('.XRthon'):
                            fp = f'{path}/{fn}'
                            
                            runner.run_forfilepath(fp)

                clsobj.environment.set_values({p : {'value' : runner.environment.values}})

                clsobj.environment.AddImportsEnvironment(runner.EnvironmentName)

                NowImport.remove(p)

            elif f'{p}.XRthon' in os.listdir(PackagesFolderPath):
                if f'{p}.XRthon' in NowImport:
                    root.raiser('LoopImportError', 'Package was loop import', number, linetext, path if not path is None else '<String>', None, root.config)
                else:
                    runner = Runner(p)
                    
                    path = f'{PackagesFolderPath}/{p}.XRthon'

                    NowImport.append(f'{p}.XRthon')

                    runner.run_forfilepath(path)
                
                    clsobj.environment.set_values({p : {'value' : runner.environment.values}})
                
                    clsobj.environment.AddImportsEnvironment(runner.EnvironmentName)

                    NowImport.remove(f'{p}.XRthon')

            elif p in BuiltinsPackages:
                if p == 'os':
                    clsobj.environment.set_values({'os' : {'value' : {
                        'environ' : os.environ,
                        'name' : os.name,
                    }}})
                elif p == 'sys':
                    clsobj.environment.set_values({'sys' : {'value' : {
                        'version' : version
                    }}})
                elif p == 'XRthon':
                    clsobj.environment.set_values({'XRthon' : {'value' : {
                        'version' : version,
                        
                    }}})
                elif p == 'this':
                    # print('This is XRthon')
                    pass
                else:
                    pass
                
            elif p in Environments.keys():
                clsobj.environment.set_values({p : {'value' : Environments[p].values}})
            
            else:
                root.raiser('NameError', 'Name is not defined', number, linetext, path if not path is None else '<String>', config=root.config)
                return

            v = 'None'

        elif linetext.split('(')[0].startswith('quit'):
            # name = linetext[4:][:-1]

            root.raiser('SystemExit', '', number, linetext, path if not path is None else '<String>', config=root.config)

            pass

        elif linetext.split('(')[0].startswith('type'):
            pass

        elif linetext.split('(')[0] in clsobj.environment.values.keys():
            # type: ignore
            name = linetext.split('(')[0]
            _= clsobj.environment.values[name]
            func: Function = _['value'] # type: ignore
            if not isinstance(func, Function):
                clsobj.raiser('TypeError', f'The name \'{func}\' is not a function', number, linetext, path if not path is None else '<String>', config=root.config)

            args_: list[str] = linetext.split('(')[1][:-1].replace(' ', '').split(',')
            if args_ == ['']:
                args_ = []
            
            args = []

            for arg in args_:
                tle = Variable.VariableLogic(clsobj, arg, number, linetext, path if not path is None else '<String>')

                arg = tle[0]

                args.append(arg)

            func.run(args)

            v = 'None'

            pass

        else:
            if '.' in linetext.split('(')[0]:
                if linetext.startswith(' '):
                    return
                _ = Variable.VariableLogic(clsobj, linetext.split('(')[0], number, linetext, path if not path is None else '<String>')
                if _[1] == 'function':
                    args_ = linetext.split('(')[1][:-1].replace(' ', '').split(',')
                    if args_ == ['']:
                        args_ = []

                    args = []

                    for arg in args_:
                        tle = Variable.VariableLogic(clsobj, arg, number, linetext, path if not path is None else '<String>')

                        arg = tle[0]

                        args.append(arg)

                    func: Function = _[0] # type: ignore

                    func.run(args) # type: ignore
            v = 'None'

        v = f'\'{v}\''.replace('\\', '\\\\')

        type_ = Str(v)

        try:
            v = eval(v)
        except Exception as e:
            if type(e) == NameError:
                root.raiser(
                            'NameError',
                            f'The name ({v}) is not defined',
                            number,
                            linetext,
                            path if not path is None else '<String>',
                            e,
                            root.config
                        )
                return
            else:
                root.raiser(
                            'SyntaxError',
                            'Invalid syntax',
                            number,
                            linetext, path if not path is None else '<String>',
                            e,
                            root.config
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
                    root.raiser(
                                'SyntaxError',
                                'Invalid syntax',
                                number,
                                linetext,
                                path if not path is None else '<String>',
                                SyntaxError('invalid syntax'),
                                root.config
                            )
                    return
            except Exception as e:
                root.raiser(
                            'SyntaxError',
                            'Invalid syntax',
                            number,
                            linetext,
                            path if not path is None else '<String>',
                            e,
                            root.config
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
                type_ = Nonetype(v)

            return v, type_, IsPrivateVariable
        except Exception as e:
            return

class Variable():
    @staticmethod
    def VariableLogic(clsobj: Runner, value: object, number: int, linetext: str, path: str):
        type_ = None # type: ignore
        
        def _a(value: str):
            if (value.startswith('"') and value.endswith('"')) \
               or (value.startswith('\'') and value.endswith('\'')):
                value = value[1:-1]
                type_ = Str(value)

            else:
                try:
                    value = '' if value == '' else eval(value) \
                        if value not in clsobj.environment.values.keys() else \
                            clsobj.environment.values[value]['value'] # type: ignore

                    t = type(value)

                    type_: Int | Float | Str | Nonetype | Object  = Int(value, number, linetext, path) if t == int \
                                else Float(value, number, linetext, path) if t == float \
                                else Str(value) if t == str \
                                else Nonetype(None) if t == NoneType \
                                else Object(value)
                except Exception as e:
                    root.raiser(
                                'SyntaxError',
                                'Invalid syntax',
                                number,
                                linetext,
                                path if not path is None else '<String>',
                                e,
                                root.config
                            )
            
            return value, type_

        value = str(value)
        if '.' in value:
            try:
                value = float(value)
                type_ = Float(value, number, linetext, path)
            except:
                parts = str(value).split('.')
                name = parts[0]
                attr_path = '.'.join(parts[1:])

                # 获取环境中的对象
                if name not in clsobj.environment.values.keys(): # type: ignore
                    value, type_ = _a(value) # type: ignore
                    return value, type_, False
                obj = clsobj.environment.values[name]['value']
                
                # 逐层获取属性或方法
                attr = obj
                for part in attr_path.split('.'):
                    _ = attr[part] # type: ignore
                    type_ = _['type'] if isinstance(_, dict) and ('type' in _) else Nonetype(None)
                    attr = _['value'] if isinstance(_, dict) else _
                
                # 执行属性或方法
                # if callable(attr):
                #     result = attr()
                # else:
                result = attr['value'] if isinstance(attr, dict) and 'value' in attr else attr
                # type_ = attr['type']
                

                return result, type_, False
        else:
            value, type_ = _a(value)
        
        return value, type_

root = Runner('root')

def config_root(config: configType):
    root.config = config

del___pycache__()
