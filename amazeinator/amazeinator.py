"""The amazeinator is totally amazing."""
import getpass


class Amazeinator:

    def __init__(self):
        self.user = getpass.getuser() or "Slartibartfast"        

    def amaze(self):
        return "{}, this is totally amazing!".format(self.user)

    def truly(self):
        return "Truly amazing."
