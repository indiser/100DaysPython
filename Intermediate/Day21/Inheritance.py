class Animal:
    def __init__(self):
        self.eyes=2
    def breathe(self):
        print("inhale,exhale")

class fish(Animal):
    def __init__(self):
        super().__init__()
    def breath(self):
        super().breathe()
        print("Under Water")
    def work(self):
        print("I am a fish")

dorry=fish()
print(f"number of eyes:{dorry.eyes}")
dorry.breath()
dorry.work()