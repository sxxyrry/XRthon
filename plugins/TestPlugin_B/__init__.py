from ...PluginAPI import (
    root,
    frames,
    parent,
    Up,
    Bottom,
    notebook,
    tk,
    JudgeVersion_Equal_Plugin,
    JudgeVersion_Greater_Plugin,
    JudgeVersion_Less_Plugin,
    FindPlugin,
    ImportPlugin,
    GetVersionForEditionLogs_Plugin,
)


_ = tk.Menu()
_.add_command(label="b", command=lambda: print("b"))
Up.add_cascade(label="b", menu=_)
