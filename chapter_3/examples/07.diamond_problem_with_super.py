class BaseClass:
    def call_me(self):
        print("Base")

class Left(BaseClass):
    def call_me(self):
        super().call_me()
        print("Left")

class Right(BaseClass):
    def call_me(self):
        super().call_me()
        print("Right")

class Sup(Left, Right):
    def call_me(self):
        super().call_me()
        print("Sup")


s = Sup()
s.call_me()
