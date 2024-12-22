from . import indrxer
import tkinter as tk
import tkinter.font as font

linenum = 0


class Liner(indrxer.IndexText):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.breakpoints = set()  # 初始化空集合用于存放断点行号
        self.y_scrollbar = tk.Scrollbar(parent)
        self.x_scrollbar = tk.Scrollbar(parent, orient='horizontal')
        self.x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.config(undo=True, xscrollcommand=self.x_scrollbar.set, yscrollcommand=self.y_scrollbar.set, wrap='none')
        self.x_scrollbar.config(command=self.xview)
        self.y_scrollbar.config(command=self.yview)
        self.font = self.settings.family
        self.font_size = self.settings.size
        self.numl = tk.Canvas(parent,
                              width=font.Font(root=parent, family=self.font, size=self.font_size).measure('0') + 5,
                              bg=self.bg, highlightthickness=0)
        self.numl.pack(side=tk.LEFT, fill=tk.BOTH)
        self.is_bold = self.settings.bold
        self.is_italic = self.settings.italic
        self.lineall = 0

    def binds(self):
        self.bind("<Key>", lambda event: self._see())
        self.bind("<Button-1>", lambda event: self._see())
        self.bind("<B2-Motion>", lambda event: self._see())
        self.bind("<MouseWheel>", lambda event: self._see())

    def _see(self):
        self.see(str(float(int(float(self.index('insert'))) + 2)))  # 一直显示光标所在行

    def update_fonts(self):
        self.config(font=(
            self.font, self.font_size, 'bold' if self.is_bold else 'normal', 'italic' if self.is_italic else 'roman'))

    def redraw(self):
        self.update_fonts()
        try:
            global linenum
            self.numl.delete("all")
            i = self.index("@0,0")
            while True:
                dline = self.dlineinfo(i)
                if dline is None:
                    break
                y = dline[1]
                linenum = str(i).split(".")[0]
                self.numl.create_text(2, y, anchor="nw", text=linenum, fill=self.line,
                                      font=(self.font, self.font_size, 'bold' if self.is_bold else 'normal',
                                            'italic' if self.is_italic else 'roman'))
                i = self.index("%s+1line" % i)

            _font = font.Font(root=self.master, family=self.font, size=self.font_size)
            w = _font.measure('0')
            self.numl.config(width=len(linenum) * w + 5) # type: ignore
            self.lineall = linenum
        except RuntimeError:
            pass

    def load_content(self, content):
        self.delete("1.0", "end")  # 删除已有内容
        self.insert("1.0", content)  # 插入新内容

    def get_text(self):
        return self.get("1.0", "end-1c")

    def set_breakpoint(self, line_number):
        self.breakpoints.add(line_number)

    def remove_breakpoint(self, line_number):
        if line_number in self.breakpoints:
            self.breakpoints.remove(line_number)
    
    def get_lineno_at_cursor(self):
        index = self.index("insert")
        return int(index.split('.')[0]) - 1  # 减一是因为Tkinter的行索引从1开始


if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-topmost", 1)
    text = Liner(root)
    text.pack(fill="both", expand=1)
    while True:  # use this instead of mainloop
        text.redraw()
        root.update()
