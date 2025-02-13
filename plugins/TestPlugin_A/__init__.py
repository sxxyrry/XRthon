from ...PluginAPI import (
    root,
    frames,
    parent,
    Up,
    Bottom,
    tk,
    JudgeVersion_Equal_Plugin,
    JudgeVersion_Greater_Plugin,
    JudgeVersion_Less_Plugin,
    FindPlugin,
    ImportPlugin,
    GetVersionForEditionLogs_Plugin
)


_ = tk.Menu()
_.add_command(label="a", command=lambda: print("a"))
Up.add_cascade(label="a", menu=_)

if FindPlugin("Y"):
    if JudgeVersion_Equal_Plugin("Y", "B--0--0.1--_indev--2025*1*1"):
        data = ImportPlugin("Y", "TestPlugin")
