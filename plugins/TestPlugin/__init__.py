from ...PluginAPI import (
    root,
    parent,
    Up,
    Bottom,
    tk,
    tkt
)

def a():
    _ = tkt.Tk(title='TestPlugin')

    t = tk.Label(_, text='TestPlugin')
    t.pack()

    _.mainloop()

_ = tk.Menu(Up)
_.add_command(label='a', command=lambda: print('TestPlugin'))
_.add_cascade(label='b', command=a)
Up.add_cascade(label='TestPlugin', menu=_)
