#method resolution orclass

class lahya():
    @property
    def lower(self):
        return '{}.{}'.format(self.first,self.last)
    def __init__(self,first,last):
        self.first = first
        self.last = last
    @property
    def islower(self):
        return '{}.{}'.format(self.first,self.last)


