from counter import Counter
from random import randrange
import tkinter
import pickle
import sys
import os

class ShinyCounter:
    def __init__(self, size, target, checkpoint, odds, memory, hunt_method):
        '''Constructor for Counter GUI'''
        self.root_window = tkinter.Tk()
        self.root_window.geometry(size)
        self.root_window.iconbitmap(self.resource_path("pokeball.ico"))
        self.root_window.resizable(False, False)
        self.root_window.title("Pokémon Shiny Counter")
        self.photo = tkinter.PhotoImage(file = self.resource_path(target))
        self.checkpoint = checkpoint
        self.odds = odds
        self.memory = memory
        self.hunt_method = hunt_method

    def resource_path(self, relative_path):
        '''Get absolute path to resource, works for dev and for PyInstaller'''
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def save(self):
        '''Saves the current count to a save file'''
        outfile = open(self.memory, "wb")
        pickle.dump(self.count.show(), outfile)
        outfile.close()

    def check_save(self):
        '''Checks if counter should save count to file'''
        return not self.count.show() % self.checkpoint

    def on_close(self):
        '''Runs when the GUI is closed'''
        if self.count.show() != self.previous_count:
            self.save()
        self.root_window.destroy()

    def key(self, event):
        '''Handles key input'''
        if event.keysym in ["space", "Up", "Right", "8", "6", "w", "d"]:
            self.count.up()
        elif event.keysym in ["Down", "BackSpace", "Left", "2", "4", "a", "s"]:
            self.count.down()
        elif event.keysym in ["Return", "5"]:
             self.count.reset()
        elif event.keysym in ["Shift_L", "Shift_R"]:
            self.save()

        if self.check_save():
            self.save()

        self.show.set("{}: {}\nOdds: {}".format(self.hunt_method, self.count.show(), self.odds))

    def run(self):
        '''Runs the GUI'''
        try:
            file = open("{}".format(self.memory), "rb")
            self.count = Counter(pickle.load(file))
            self.previous_count = self.count.show()
            file.close()
        except:
            self.count = Counter()
            self.previous_count = 0
        p = tkinter.Label(self.root_window, image = self.photo)
        p.photo = self.photo
        p.pack(side = tkinter.TOP)
        self.show = tkinter.StringVar()
        info = tkinter.Label(self.root_window, textvariable = self.show)
        info.config(font = ("TkDefaultFont", 20))
        self.show.set("{}: {}\nOdds: {}".format(self.hunt_method, self.count.show(), self.odds))
        info.pack(side = tkinter.TOP)
        self.root_window.bind("<KeyPress>", self.key)
        self.root_window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root_window.mainloop()

if __name__ == "__main__":
    size = "300x250"
    target = "shiny_rookidee.gif"
    checkpoint = 5
    odds = "1/1365"
    memory = "shiny_rookidee_count.cnt"
    hunt_method = "Eggs Hatched"
    ShinyCounter(size = size, target = target, checkpoint = checkpoint, odds = odds, memory = memory, hunt_method = hunt_method).run()
