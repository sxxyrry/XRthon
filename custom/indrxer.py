from . import color
import os
import tkinter as tk


class IndexText(color.XRColorText):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.i = 0
        self.bind("<Return>", lambda event: self.enter())
        self.bind("<Key>", lambda event: self.character_completion(event))
        self.bind("<BackSpace>", lambda event: self.backspace())
        self.bind("<Tab>", lambda event: self.tab())
        self.bind('<Shift-Tab>', lambda event: self.untab())

    def enter(self):
        self.see(str(float(int(float(self.index('insert'))) + 2)))
        self.i = 0
        a = self.index('insert')
        aa = int(float(a))
        b = self.get(float(aa), a).replace('\n', '')
        c = b
        if b[-1:] == ':':
            i = 0
            while True:
                if b[:4] == '    ':
                    b = b[4:]
                    i += 1
                else:
                    break
            self.i = i + 1
        else:
            i = 0
            while True:
                if b[:4] == '    ':
                    b = b[4:]
                    i += 1
                else:
                    break
            self.i = i
            try:
                a = c.strip().split()[0]
            except IndexError:
                a = ''
            if c.strip() == 'break' or c.strip() == 'pass' or c.strip() == 'continue':
                self.i -= 1
            elif a in ['raise', 'return']:  # 因为return、raise后可能有值，故特殊处理
                self.i -= 1
        self.insert('insert', '\n')
        for j in range(self.i):
            self.insert('insert', '    ')
        return 'break'

    def backspace(self):
        _dict = {'(': ')', '{': '}', '[': ']', '"': '"', "'": "'"}
        last = str(int(''.join(list(self.index('insert'))[
                               (-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1)):])) - 1)
        all_insert = ''.join(list(self.index('insert'))[
                             :(-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1))]) + last
        a = self.get(all_insert, 'insert')
        if a in ['(', '{', '[', '"', "'"]:
            last = str(int(''.join(list(self.index('insert'))[
                                   (-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1)):])) + 1)
            all_insert = ''.join(list(self.index('insert'))[
                                 :(-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1))]) + last
            b = self.get('insert', all_insert)
            if b == _dict[a]:  # 符合条件，删除2个
                last1 = str(int(''.join(list(self.index('insert'))[
                                        (-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1)):])) - 1)
                all_insert1 = ''.join(list(self.index('insert'))[
                                      :(-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1))]) + last1
                last2 = str(int(''.join(list(self.index('insert'))[
                                        (-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1)):])) + 1)
                all_insert2 = ''.join(list(self.index('insert'))[
                                      :(-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1))]) + last2
                self.delete(all_insert1, all_insert2)
                return 'break'
        else:
            last1 = str(int(''.join(list(self.index('insert'))[
                                    (-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1)):])) - 4)
            all_insert1 = ''.join(list(self.index('insert'))[
                                  :(-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1))]) + last1
            if self.get(all_insert1, 'insert') == '    ':
                self.delete(all_insert1, 'insert')
                return 'break'

    def character_completion(self, event):  # 字符补全（对【(】、【[】、【{】等进行自动补全）
        a = event.keysym
        if a == 'parenleft':  # (
            self.insert("insert", ')')
            last = str(int(''.join(list(self.index('insert'))[
                                   (-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1)):])) - 1)
            all_insert = ''.join(list(self.index('insert'))[
                                 :(-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1))]) + last
            self.mark_set('insert', all_insert)
        elif a == 'braceleft':  # {
            self.insert("insert", '}')
            last = str(int(''.join(list(self.index('insert'))[
                                   (-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1)):])) - 1)
            all_insert = ''.join(list(self.index('insert'))[
                                 :(-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1))]) + last
            self.mark_set('insert', all_insert)
        elif a == 'bracketleft':  # [
            self.insert("insert", ']')
            last = str(int(''.join(list(self.index('insert'))[
                                   (-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1)):])) - 1)
            all_insert = ''.join(list(self.index('insert'))[
                                 :(-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1))]) + last
            self.mark_set('insert', all_insert)
        elif a == 'quotedbl':
            self.insert("insert", '"')
            last = str(int(''.join(list(self.index('insert'))[
                                   (-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1)):])) - 1)
            all_insert = ''.join(list(self.index('insert'))[
                                 :(-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1))]) + last
            self.mark_set('insert', all_insert)
        elif a == "apostrophe":
            self.insert("insert", "'")
            last = str(int(''.join(list(self.index('insert'))[
                                   (-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1)):])) - 1)
            all_insert = ''.join(list(self.index('insert'))[
                                 :(-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1))]) + last
            self.mark_set('insert', all_insert)

    def insert_get(self):
        start = tk.SEL_FIRST
        end = tk.SEL_LAST
        is_insert = True if self.get(start, end) != '' else False
        return is_insert, self.index(start), self.index(end)

    def tab(self):
        is_insert, start, end = self.insert_get()
        if not is_insert:
            self.insert('insert', '    ')
        else:
            start = int(float(start))
            end = int(float(end))
            for i in range(start, end + 1):
                self.insert(str(float(i)), '    ')
        return 'break'

    def untab(self):
        is_insert, start, end = self.insert_get()
        if not is_insert:
            last = str(int(''.join(list(self.index('insert'))[
                                   (-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1)):])) - 4)
            all_insert = ''.join(list(self.index('insert'))[
                                 :(-1 * (len(os.path.splitext(self.index('insert'))[-1]) - 1))]) + last
            if self.get(all_insert, 'insert') == '    ':
                self.delete(all_insert, 'insert')
        else:
            start = self.index(start)
            end = self.index(end)
            for i in range(int(float(start)), int(float(end)) + 1):
                last = str(int(''.join(list(self.index(str(float(i))))[
                                       (-1 * (len(os.path.splitext(self.index(str(float(i))))[-1]) - 1)):])) + 4)
                all_insert = ''.join(list(self.index(str(float(i))))[
                                     :(-1 * (len(os.path.splitext(self.index(str(float(i))))[-1]) - 1))]) + last
                if self.get(str(float(i)), all_insert) == '    ':
                    self.delete(str(float(i)), all_insert)
        return 'break'


if __name__ == "__main__":
    root = tk.Tk()
    text = IndexText(root, font=("黑体", 30))
    text.pack()
    root.mainloop()
