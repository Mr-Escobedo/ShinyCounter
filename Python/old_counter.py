class Counter:
    '''Counter class for various uses'''
    def __init__(self, count = 0, step = 1, negative = False):
        '''Constructor for Counter class instance'''
        self.count = count
        self.step = step
        self.negative = negative
    def __repr__(self):
        '''Returns current state of Counter instance'''
        return "Counter(count = {}, step = {})".format(self.count, self.step)
    def __str__(self):
        '''Used when Counter instance is passed into print() or str()'''
        return "Count: {}".format(self.count)
    def __int__(self):
        '''Used when Counter instance is passed into int()'''
        return self.count
    def __add__(self, right):
        '''Used to add numbers or another Counter instance'''
        if type(right) == Counter:
            self.count += right.count
        else:
            self.count += right
        return Counter(self.count, self.step)
    def __radd__(self, right):
        '''Used in reverse of add'''
        return self.__add__(right)
    def __sub__(self, right):
        '''Subtracts number or another Counter instance'''
        if type(right) == Counter:
            self.count -= right.count
        else:
            self.count -= right
        return Counter(self.count, self.step)
    def __rsub__(self, right):
        '''Used in reverse of sub'''
        return self.__sub__(right)
    def __eq__(self, right):
        '''Determines if this Counter instance is equal to another'''
        return self.count == right.count and self.step == right.step
    def __lt__(self, right):
        '''Determines if this Counter instance has a lower count'''
        return self.count < right.count
    def __le__(self, right):
        return self.count < right.count or self.count == right.count
    def up(self):
        '''Increments the counter'''
        self.count += self.step
    def down(self):
        '''Decrements the counter if current count is positive'''
        if self.count > 0 or (self.count <= 0 and self.negative):
            self.count -= self.step
    def show(self):
        '''Returns the current count'''
        return self.count
    def reset_count(self, new_count = 0):
        '''Resets the count to new value'''
        self.count = new_count
    def reset_step(self, new_step = 1):
        '''Resets the step to new value'''
        self.step = new_step
    def invert_negative(self):
        '''Negates the counter's current ability to go further negative'''
        self.negative = not self.negative

    
if __name__ == "__main__":
    c = Counter()
