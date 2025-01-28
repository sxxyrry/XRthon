from ...PluginAPI import (
    root,
    frames,
    parent,
    Up,
    Bottom,
    tk,
    tkt,
    os,
    folder,
    Warning_log,
    filedialog
)

XRthonFeatures_menu = tk.Menu(Up)

XRthonFeatures_menu.add_command(
    label="XRthon Interactive Mode",
    command=lambda: os.startfile(os.path.join(folder, "./../XRthon.py"))
)

def run():
    path = filedialog.askopenfilename(
            defaultextension='.XRthon',
            filetypes=[("XRthon File", "*.XRthon")],
            title='Choose File'
    )

    if path:
        os.startfile(
            os.path.join(folder, "./../XRthon.py"),
            arguments=path
        )
    else:
        Warning_log.warning("AddSomeXRthonFeaturesToEditor: No file selected.")

XRthonFeatures_menu.add_command(
    label="Run File In XRthon Window",
    command=run
)

Up.add_cascade(label="XRthon Features", menu=XRthonFeatures_menu)
