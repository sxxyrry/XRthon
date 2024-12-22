import tkinter as tk
import re
import idlelib.colorizer as idc
import idlelib.percolator as idp
import keyword
from . import config
from . import basictext


class XRColorText(basictext.BaseText):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        idc.color_config(self)
        self.focus_set()
        self.p = idp.Percolator(self)
        self.d = idc.ColorDelegator()
        self.p.insertfilter(self.d)
        self.settings = config.Settings()
        self.bg = self.settings.bg
        self.normal = self.settings.normal
        self.comment = self.settings.comment
        self.keywords = self.settings.keywords
        self.builtin = self.settings.builtin
        self.string = self.settings.string
        self.definition = self.settings.definition
        self.symbol = self.settings.symbol
        self.classmode = self.settings.classmode
        self.line = self.settings.line
        self.number = self.settings.number
        self.color_text(True)
        self.config(cursor='I-beam')

    @staticmethod
    def make_pat():
        kwlist = [
                #   'raise',
                #   'return',
                #   'init',
                #   'def',
                #   'if',
                #   'for',
                #   'end',
                #   'del',
                #   'import',
                #   'python',
                  ]
        funcs = [
                 'print',
                 'input',
                #  'VariableError',
                #  'InitError',
                #  'CodeError',
                #  'ErrortypeError',
                #  'NameError',
                #  'EmptyFunctionError',
                #  'LogicError',
                #  'ConditionError',
                #  'TextError',
                #  'EmptyIterableError',
                #  'NotSupportError',
                #  'CanNotDeleteError',
                #  'PrintError',
                #  'del.AllVariablesDelete',
                #  'SYS.Var',
                #  'type',
                 ]

        def _any(name, alternates):
            return "(?P<%s>" % name + "|".join(alternates) + ")"

        sl = [r'\=', r'\{', r'\}', r'\:', r'\,', r'\.',]
        kw = r"\b" + _any("KEYWORD", kwlist) + r"\b" 
        symbol_a = r"\b" + _any("SYMBOL1", sl) + r"\b"
        symbol_b = _any("SYMBOL2", sl) + r"\b"
        symbol_c = r"\b" + _any("SYMBOL3", sl)
        symbol_d = _any("SYMBOL4", sl)
        symbol_e = _any("SYMBOL5", sl) + r'[^\n]*'
        symbol_f = r"\b" + _any("SYMBOL6", sl) + r'[^\n]*'
        builtinlist = [str(name) for name in funcs
                       if not name.startswith('_') and
                       name not in keyword.kwlist]
        # builtin = r"([^.'\"\\#]\b|^)" + _any("BUILTIN", builtinlist) + r"\b"
        builtin = r"\b" + _any("BUILTIN", builtinlist) + r"\b"
        comment = _any("COMMENT", [r"#[^\n]*"])
        number = _any("NUM", [r"\b[0-9]+(?![0-9]+)\b"])
        dqstring = r"'[^\"\\\n]*(\\.[^\"\\\n]*)*'?"
        string = _any("STRING", [dqstring])
        prog = re.compile("|".join([
            builtin, comment, string, kw, symbol_b, symbol_c,
            symbol_d, symbol_a, symbol_e, symbol_f, number,
            _any("SYNC", [r"\n"]),
        ]),
            re.DOTALL | re.MULTILINE)
        return prog

    def color_text(self, is_color):  # is_color:是否上色
        self.config(background=self.bg, foreground=self.normal)
        try:
            self.p.removefilter(self.d)
        except AssertionError:
            pass
        self.d = idc.ColorDelegator()
        self.d.prog = self.make_pat()
        if is_color:
            self.d.tagdefs['COMMENT'] = {'foreground': self.comment}
            self.d.tagdefs['KEYWORD'] = {'foreground': self.keywords}
            self.d.tagdefs['BUILTIN'] = {'foreground': self.builtin}
            self.d.tagdefs['STRING'] = {'foreground': self.string}
            self.d.tagdefs['DEFINITION'] = {'foreground': self.definition}
            self.d.tagdefs['SYMBOL1'] = {'foreground': self.symbol}
            self.d.tagdefs['SYMBOL2'] = {'foreground': self.symbol}
            self.d.tagdefs['SYMBOL3'] = {'foreground': self.symbol}
            self.d.tagdefs['SYMBOL4'] = {'foreground': self.symbol}
            self.d.tagdefs['SYMBOL5'] = {'foreground': self.symbol}
            self.d.tagdefs['SYMBOL6'] = {'foreground': self.symbol}
            self.d.tagdefs['CLASSMODE'] = {'foreground': self.classmode}
            self.d.tagdefs['NUM'] = {'foreground': self.number}
        else:
            self.d.tagdefs['COMMENT'] = {'foreground': self.normal}
            self.d.tagdefs['KEYWORD'] = {'foreground': self.normal}
            self.d.tagdefs['BUILTIN'] = {'foreground': self.normal}
            self.d.tagdefs['STRING'] = {'foreground': self.normal}
            self.d.tagdefs['DEFINITION'] = {'foreground': self.normal}
            self.d.tagdefs['SYMBOL1'] = {'foreground': self.normal}
            self.d.tagdefs['SYMBOL2'] = {'foreground': self.normal}
            self.d.tagdefs['SYMBOL3'] = {'foreground': self.normal}
            self.d.tagdefs['SYMBOL4'] = {'foreground': self.normal}
            self.d.tagdefs['SYMBOL5'] = {'foreground': self.normal}
            self.d.tagdefs['SYMBOL6'] = {'foreground': self.normal}
            self.d.tagdefs['CLASSMODE'] = {'foreground': self.normal}
            self.d.tagdefs['NUM'] = {'foreground': self.normal}
        try:
            self.p.insertfilter(self.d)
        except AssertionError:
            pass

    def update_color(self, is_color):
        self.bg = self.settings.bg
        self.normal = self.settings.normal
        self.comment = self.settings.comment
        self.keywords = self.settings.keywords
        self.builtin = self.settings.builtin
        self.string = self.settings.string
        self.definition = self.settings.definition
        self.symbol = self.settings.symbol
        self.classmode = self.settings.classmode
        self.line = self.settings.line
        self.number = self.settings.number
        self.color_text(is_color)


if __name__ == '__main__':
    root = tk.Tk()
    text = XRColorText(root, font=("黑体", 30))
    text.pack()
    root.mainloop()
