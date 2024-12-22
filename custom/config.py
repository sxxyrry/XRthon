import platform
class Settings:
    def __init__(self):
        self.bg = "#ffffff"
        self.normal = '#000000'
        self.comment = "#C0C0C0"
        self.keywords = "#00BFFF"
        self.builtin = "#7B68EE"
        self.string = "#FFA500"
        self.definition = "#228B22"
        self.symbol = "#FF0000"
        self.classmode = "#DA70D6"
        self.line = "#717171"
        self.number = "#000000"
        self.size = 15
        self.bold = False
        self.italic = False
        os_type = platform.system()
        if os_type == "Darwin":
            self.family = "Ayuthaya"
            self.bigkey = "Command"
        else:
            self.family = "Consolas"
            self.bigkey = "Control"
