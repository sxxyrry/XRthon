from custom.CustomNotebook import CustomNotebook
from custom.liner import Liner
import tkinter as tk, tkintertools as tkt
from tkinter import filedialog, messagebox, scrolledtext
from Runner import Runner
from typing import Literal
import tkinter.ttk as ttk
import _tkinter as _tk
from folder import folder
from Edition_logs import (
    English_Edition_logsForEditor,
    English_Edition_logsForXRthon,
)
from VersionSystem import (
    VersionSystem,
    VersionSystemRulesMDFileContent,
)
from versions import (
    GetVersionForXRthon,
    GetVersionForEditor,
)
from logs import (
    Check_log,
    Plugins_log,
    Runner_log,
    Warning_log,
)
import os
import sys
from colorama import Fore, Style, init


root = tkt.Tk("XRthon Editor")
frames: list[tuple[tk.Frame, Liner]] = []
parent = tk.Frame(root)
Up = tk.Menu(parent)
Bottom = tk.Frame(parent)
notebook = CustomNotebook(parent)
