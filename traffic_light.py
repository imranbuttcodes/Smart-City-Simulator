class Traffic:
    def __init__(self,location):
        self.location = location
        self.idx = 0
        self.states = ["red",'green','yellow']
    def change_state(self):
        if self.idx == 2:
            self.idx = 0
        self.idx += 1
        
    def __str__(self):
        return f"Current State: {self.states[self.idx]}"

