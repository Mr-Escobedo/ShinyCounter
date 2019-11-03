from counter import Counter
import tkinter
import pickle

class ShinyCounter:
    def __init__(self, size, target, checkpoint, odds, memory, hunt_method):
        '''Constructor for Counter GUI'''
        self.root_window = tkinter.Tk()
        self.root_window.geometry(size)
        self.root_window.iconbitmap("pokeball.ico")
        self.root_window.resizable(False, False)
        self.root_window.title("Pokémon Shiny Counter")
        self.photo = tkinter.PhotoImage(file = target)
        self.checkpoint = checkpoint
        self.odds = odds
        self.memory = memory
        self.hunt_method = hunt_method

    def save(self) -> None:
        '''Saves the current count to a save file'''
        outfile = open(self.memory, "wb")
        pickle.dump(self.count.show(), outfile)
        outfile.close()

    def check_save(self) -> bool:
        '''Determines if the Shiny Counter should save'''
        return not self.count.show() % self.checkpoint

    def key(self, event) -> None:
        '''Handles key input'''
        if event.keysym in ["space", "Up", "Right", "8", "6", "w", "d"]:
            self.count.up()
        elif event.keysym in ["Down", "BackSpace", "Left", "2", "4", "a", "s"]:
            self.count.down()
        elif event.keysym in ["Return", "5"]:
            self.count.reset_count()
        elif event.keysym in ["Shift_L", "Shift_R"]:
            self.save()

        if self.check_save():
            self.save()

        self.show.set("{}: {}\nOdds: {}".format(self.hunt_method, self.count.show(), self.odds))

    def run(self):
        '''Runs the GUI'''
        try:
            file = open("{}".format(self.memory), "rb")
            self.count = Counter(count = pickle.load(file))
            file.close()
        except:
            self.count = Counter()
        p = tkinter.Label(self.root_window, image = self.photo)
        p.photo = self.photo
        p.pack(side = tkinter.TOP)
        self.show = tkinter.StringVar()
        info = tkinter.Label(self.root_window, textvariable = self.show)
        self.show.set("{}: {}\nOdds: {}".format(self.hunt_method, self.count.show(), self.odds))
        info.pack(side = tkinter.TOP)
        self.root_window.bind("<KeyPress>", self.key)
        self.root_window.mainloop()

if __name__ == "__main__":
    size = "300x135"
    target = "shiny_rowlet.gif"
    checkpoint = 5
    odds = "1/512"
    memory = "shiny_rowlet_count.cnt"
    hunt_method = "Eggs Hatched"
    ShinyCounter(size = size, target = target, checkpoint = checkpoint, odds = odds, memory = memory, hunt_method = hunt_method).run()
