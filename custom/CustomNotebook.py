import tkinter.ttk as ttk
import tkinter as tk


class CustomNotebook(ttk.Notebook):
    """A ttk Notebook with close buttons on each tab"""

    __initialized = False

    def __init__(self, *args, **kwargs): # type: ignore
        if not self.__initialized:
            try:
                self.__initialize_custom_style()
            except tk.TclError:
                pass
            self.__initialized = True
            self._protected_indices: set[int] = set()

        kwargs["style"] = "CustomNotebook"
        ttk.Notebook.__init__(self, *args, **kwargs) # type: ignore

        self._active = None

        self.bind("<ButtonPress-1>", self.on_close_press, True) # type: ignore
        self.bind("<ButtonRelease-1>", self.on_close_release) # type: ignore

    def protect_tab(self, index: int):
        """Mark the tab of the specified index as protected"""
        self._protected_indices.add(index)

    def unprotect_tab(self, index: int):
        """Deselect the protection status of the tab for the specified index"""
        if index in self._protected_indices:
            self._protected_indices.remove(index)

    def on_close_press(self, event: tk.Event): # type: ignore
        """Called when the button is pressed over the close button"""

        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y)) # type: ignore
            if index in self._protected_indices:
                pass
            else:
                self.state(['pressed']) # type: ignore
                self._active = index # type: ignore
                frame: tk.Frame = self.nametowidget(self.tabs()[index]) # type: ignore
                frame.event_generate("<<NotebookTabClosed>>")

    def on_close_release(self, event: tk.Event): # type: ignore
        """Called when the button is released over the close button"""
        if not self.instate(['pressed']): # type: ignore
            return

        element = self.identify(event.x, event.y)
        index = self.index("@%d,%d" % (event.x, event.y)) # type: ignore

        if "close" in element and self._active == index: # type: ignore
            self.forget(index) # type: ignore

        self.state(["!pressed"]) # type: ignore
        self._active = None

    # def add(self, page: tk.Frame, text: str, sticky="ew", **kwargs):
    #     self.frames.append(page)
    #     # ttk.Notebook.add(self, page, text=text, sticky=sticky, **kwargs)
    #     self.add_(page, text=text, sticky=sticky, **kwargs)
    #     self.update()

    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            tk.PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0CBHSU1aQACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            tk.PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            tk.PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )

        style.element_create("close", "image", "img_close", # type: ignore
                             ("active", "pressed", "!disabled", "img_closepressed"),
                             ("active", "!disabled", "img_closeactive"), border=8, sticky='')
        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})]) # type: ignore
        style.layout("CustomNotebook.Tab", [ # type: ignore
            ("CustomNotebook.tab", {
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                ]
                            })
                        ]
                    })
                ]
            })
        ])
        style.configure("CustomNotebook", background="white", fieldbackground="white", foreground="black") # type: ignore
        style.map("CustomNotebook.Tab", background=[("selected", "white")], foreground=[("selected", "black")]) # type: ignore