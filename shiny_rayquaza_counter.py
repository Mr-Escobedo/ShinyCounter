import tkinter
import pickle

class Counter:
    def __init__(self, count = 0, step = 1):
        self.count = count
        self.step = step
    def __repr__(self):
        return "Counter({},{})".format(self.count. self.step)
    def __str__(self):
        return "Count: {}".format(self.count)
    def up(self):
        self.count += self.step
    def down(self):
        if self.count == 0:
            self.count -= 0
        else:
            self.count -= self.step
    def reset(self):
        self.count = 0
    def show(self):
        return self.count

            
class ShinyCounter:
    def __init__(self):
        self.root_window = tkinter.Tk()
        self.root_window.geometry("300x200")
        self.root_window.iconbitmap("pokeball.ico")
        self.root_window.resizable(0,0)
        self.root_window.title("Pokémon Shiny Counter")
        self.photo = tkinter.PhotoImage(file="rayquaza.gif")
        self.memory = "shiny_rayquaza_count.cnt"

    def save(self):
        outfile = open(self.memory, 'wb')
        pickle.dump(self.count.show(), outfile)
        outfile.close()

    def key(self,event):
        if event.keysym == "space" or event.keysym == "Up" or event.keysym == "Right" or event.keysym == '8' or event.keysym == '6':
            self.count.up()
        elif event.keysym == "Down" or event.keysym == "BackSpace" or event.keysym == "Left" or event.keysym == '2' or event.keysym == '4':
            self.count.down()
        elif event.keysym == "Return" or event.keysym == '5':
            self.count.reset()
        elif event.keysym == 'Shift_L' or event.keysym == 'Shift_R':
            self.save()
            
        if self.count.show() % 10 == 0:
            self.save()
            
        self.show.set("Soft Resets: {}\nOdds: 1/1365".format(self.count.show()))
        
    def run(self):
        try:
            file = open('{}'.format(self.memory), 'rb')
            self.count = Counter(pickle.load(file))
        except FileNotFoundError:
            self.count = Counter()
        except pickle.UnpicklingError:
            self.count = Counter()
        except:
            self.count = Counter()
        p = tkinter.Label(self.root_window, image= self.photo)
        p.photo = self.photo
        p.pack(side=tkinter.TOP)
        self.show = tkinter.StringVar()
        info = tkinter.Label(self.root_window, textvariable = self.show)
        self.show.set("Soft Resets: {}\nOdds: 1/1365".format(self.count.show()))
        info.pack(side=tkinter.TOP)
        self.root_window.bind("<KeyPress>", self.key)
        self.root_window.mainloop()
        


if __name__ == '__main__':
    ShinyCounter().run()
