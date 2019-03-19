from collections import UserList
class ClExTest(UserList):
    def __init__(self, col=None):
        if col is None:
            UserList.__init__(self)
        else:
            UserList.__init__(self, col)    
    
    def yieldList(self):
        for el in self:
            yield(el)
