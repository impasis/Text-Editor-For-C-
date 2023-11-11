"""
TE++ - Text Editor for C++:
Version - 1.2
Color Theme - Monokai
"""

from tkinter import *
from tkinter import filedialog
import webbrowser
import ctypes
import re
import os


class Editor:
    def __init__(self, window):
        self.win = window
        self.main_entry = Text(master=self.win, width=200, height=100, font=('Consolas', 15),
            background=bg_color, foreground=txt_color, insertbackground=txt_color,
            relief=FLAT, borderwidth=30, tabs=56)
        # self.main_entry.bind("<keyRelease>")

    def draw(self):
        lbl = Label(master=self.win, width=600, height=2, background=bg_color)
        lbl.pack()
        self.main_entry.pack(fill=BOTH, expand=1)


class Main:
    def __init__(self, width, height, title, screen, local_editor, local_name):
        self.width = width
        self.height = height
        self.title = title
        self.screen = screen
        self.editor = local_editor
        self.name = local_name
        self.cmd_win = None
        self.command_text = ""
        self.cmd_entry = None
        self.cmd_directory = None
        self.prev_text = ""

    def open_file(self, event=None):
        filepath = filedialog.askopenfilename()
        # print(name)
        if filepath != "":
            self.name = filepath
            st = filepath.split('/')
            self.screen.title(f"{self.name} - TE++ (1.2)")
            new = ''
            for el in st[:-1]:
                new += el + '\\'
            self.cmd_directory = new
            with open(filepath, "r") as file:
                text = file.read()
                self.editor.main_entry.delete("1.0", END)
                self.editor.main_entry.insert("1.0", text)
            self.syntax()
        # print(name)

    # Global save for rename or create file
    def save_file(self, event=None):
        filepath = filedialog.asksaveasfilename()
        if filepath != "":
            st = filepath.split('/')
            new = ''
            for el in st[:-1]:
                new += el + '\\'
            self.cmd_directory = new

            self.name = filepath
            self.screen.title(f"{self.name} - TE++ (1.2)")

            text = self.editor.main_entry.get("1.0", END)
            with open(filepath, "w") as file:
                file.write(text)

    # Just Ctrl+S
    def fast_save_file(self, event=None):
        # print(name)
        if self.name != "":
            text = self.editor.main_entry.get("1.0", END)
            with open(self.name, "w") as file:
                file.write(text)

    def write_command(self):
        if self.cmd_entry:
            self.command_text = self.cmd_entry.get("1.0", END)
            self.cmd_win.destroy()

    def start_compilation(self, event=None):
        if self.cmd_directory:
            # print(self.cmd_directory)
            # print(self.cmd_directory)
            for st in self.command_text.splitlines():
                os.system(st)

    def choice_command(self):
        self.cmd_win = Tk()
        self.cmd_win.title('Commands')
        self.cmd_win.geometry("500x500")
        self.cmd_win["bg"] = bg_color
        if self.cmd_win:
            self.cmd_entry = Text(master=self.cmd_win, width=150, height=14, font=('Consolas', 15),
                background=bg_color, foreground=txt_color, insertbackground=txt_color)
            self.cmd_entry.insert("1.0", self.command_text)
            lbl = Label(master=self.cmd_win, text="Necessary commands:", height=2,
                background=bg_color, foreground=txt_color)
            btn = Button(self.cmd_win, text="OK", width=10, height=3, command=self.write_command,
                background=bg_color, foreground=txt_color)
            lbl.pack()
            self.cmd_entry.pack()
            btn.pack()

    def syntax(self, event=None):
        if self.editor.main_entry.get('1.0', END) == self.prev_text:
            return

        for st in self.editor.main_entry.tag_names():
            self.editor.main_entry.tag_remove(st, '1.0', 'end')

        i = 0
        for syms, color in repl:
            for start, end in self.search(syms):
                self.editor.main_entry.tag_add(f"{i}", start, end)
                self.editor.main_entry.tag_config(f"{i}", foreground=color)

                i += 1
        self.prev_text = self.editor.main_entry.get('1.0', END)

    def search(self, syms, groupid=0):
        matches = []

        text = self.editor.main_entry.get('1.0', END).splitlines()

        for i, line in enumerate(text):
            for match in re.finditer(syms, line):
                matches.append(
                    (f"{i + 1}.{match.start()}", f"{i + 1}.{match.end()}")
                )

        return matches

    def open_link(self):
        webbrowser.open_new("https://github.com/impasis/Text-Editor-For-C-/blob/main/README.md")

    # Func. for a create and draw buttons
    def buttons(self):
        btn_open = Button(self.screen, text='Open File', command=self.open_file)
        btn_save_as = Button(self.screen, text='Save As', command=self.save_file)
        btn_save = Button(self.screen, text='Save', command=self.fast_save_file)
        btn_create = Button(self.screen, text="New File", command=create_file)
        btn_cmd = Button(self.screen, text="Commands", command=self.choice_command)
        btn_run = Button(self.screen, text="▶", command=self.start_compilation)
        btn_help = Button(self.screen, text="Help", command=self.open_link)
        btn_close = Button(self.screen, text="X", command=self.screen.destroy)
        btn_open.place(x=0, y=0, width=80, height=36)
        btn_save.place(x=80, y=0, width=80, height=36)
        btn_save_as.place(x=160, y=0, width=80, height=36)
        btn_create.place(x=240, y=0, width=80, height=36)
        btn_cmd.place(x=320, y=0, width=80, height=36)
        btn_run.place(x=400, y=0, width=80, height=36)
        btn_help.place(x=480, y=0, width=80, height=36)
        btn_close.place(x=560, y=0, width=80, height=36)

    """def close(event=None):
        self.screen.destroy(event=None) - toshe samoe"""

    # Main of main's
    def run(self, st):
        if st == "OK":
            self.screen.iconbitmap("ico.ico")
            self.screen.title(self.title)
            self.screen.geometry(f"{self.width}x{self.height}")
            self.editor.draw()
            self.buttons()
            self.editor.main_entry.bind('<KeyRelease>', self.syntax)

            self.syntax()
            self.screen.bind("<Control-s>", self.fast_save_file)   
            self.screen.bind("<Key-F5>", self.start_compilation)
            self.screen.bind("<Control-o>", self.open_file)
            self.screen.bind("<Control-n>", create_file)
            # self.screen.bind("<Control-x>", self.close) - pomoika
            self.screen.mainloop()


"""
def test(event=None):
    print("HELLO")
"""

# Func. for new window:)s
def create_file(event=None):
    global name

    new_name = ""
    new_win = Tk()
    new_editor = Editor(new_win)
    new_app = Main(640, 695, "untitled", new_win, new_editor, new_name)
    new_app.run("OK")


def rgbToHex(rgb):
    return "#%02x%02x%02x" % rgb


ctypes.windll.shcore.SetProcessDpiAwareness(True)
bg_color = rgbToHex((40, 40, 40))
txt_color =rgbToHex((234, 234, 234))
keywords = rgbToHex((249, 36, 114))
comments = rgbToHex((110,105,89))
string = rgbToHex((231, 219, 116))
grid = rgbToHex((162, 215, 193))
numbers = rgbToHex((172,128,255))
win = Tk()
editor = Editor(win)
name = ""
repl = [
    ['(^|\t| )(typedef|const|using|namespace|for|while|return|if|else|and|or|not|switch|case|int|char|bool|long long|long int|long|long char|long bool|template|typename|printf|size_t|fopen|fclose|struct|class|string)( $|)', keywords],
    ['(^|(|)| )(#include|#define|#if|#else|#else|#endif|#ifndef|)($| )', grid],
    ['(false|true)', numbers],
    ['<.*?>', string],
    ['".*?"', string],
    ['\'.*?\'', string],
    ['//.*?$', comments],
]

if __name__ == "__main__":
    app = Main(640, 695, "untitled", win, editor, name)
    app.run("OK")
