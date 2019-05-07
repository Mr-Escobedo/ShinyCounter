class Counter:
    '''Class for Counter'''
    def __init__(self, count = 0, step = 1):
        '''Constructor for Counter'''
        self.count = count
        self.step = step
    def __repr__(self):
        '''Returns current state of Counter instance'''
        return "Counter({}, {})".format(self.count, self.step)
    def __str__(self):
        '''Used when Counter instance is passed into print()'''
        return "Count: {}".format(self.count)
    def __int__(self):
        '''Used when a Counter instance is passed into int()'''
        return self.count
    def up(self):
        '''Increments the count'''
        self.count += self.step
    def down(self):
        '''Decrements the count if the current count is positive'''
        if self.count > 0:
            self.count -= self.step
    def reset(self):
        '''Sets the current count to 0'''
        self.count = 0
    def set_step(self, step = 1):
        '''Resets the step'''
        self.step = step
    def show(self):
        '''Returns the current count'''
        return self.count
