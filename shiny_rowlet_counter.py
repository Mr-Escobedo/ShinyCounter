from counter import Counter
import tkinter
import pickle

class ShinyCounter:
    def __init__(self):
        '''Constructor for Counter GUI'''
        self.root_window = tkinter.Tk()
        self.root_window.geometry("300x150")
        self.root_window.iconbitmap("pokeball.ico")
        self.root_window.resizable(False, False)
        self.root_window.title("Pokémon Shiny Counter")
        self.photo = tkinter.PhotoImage(file = "shiny_rowlet.gif")
        self.checkpoint = 5
        self.odds = "1/512"
        self.memory = "shiny_rowlet_count.cnt"

    def save(self):
        '''Saves the current count to a save file'''
        outfile = open(self.memory, "wb")
        pickle.dump(self.count.show(), outfile)
        outfile.close()

    def key(self, event):
        '''Handles key input'''
        if event.keysym in ["space", "Up", "Right", "8", "6"]:
            self.count.up()
        elif event.keysym in ["Down", "BackSpace", "Left", "2", "4"]:
            self.count.down()
        elif event.keysym in ["Return", "5"]:
            self.count.reset()
        elif event.keysym in ["Shift_L", "Shift_R"]:
            self.save()

        if self.count.show() % self.checkpoint == 0:
            self.save()

        self.show.set("Eggs Hatched: {}\nOdds: {}".format(self.count.show(), self.odds))

    def run(self):
        '''Runs the GUI'''
        try:
            file = open("{}".format(self.memory), "rb")
            self.count = Counter(count = pickle.load(file), step = 1)
        except:
            self.count = Counter()
        p = tkinter.Label(self.root_window, image = self.photo)
        p.photo = self.photo
        p.pack(side = tkinter.TOP)
        self.show = tkinter.StringVar()
        info = tkinter.Label(self.root_window, textvariable = self.show)
        self.show.set("Eggs Hatched: {}\nOdds: {}".format(self.count.show(), self.odds))
        info.pack(side = tkinter.TOP)
        self.root_window.bind("<KeyPress>", self.key)
        self.root_window.mainloop()

if __name__ == "__main__":
    ShinyCounter().run()
