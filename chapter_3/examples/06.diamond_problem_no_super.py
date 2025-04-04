class BaseClass:
    def call_me(self):
        print("Base")

class Left(BaseClass):
    def call_me(self):
        BaseClass.call_me(self)
        print("Left")

class Right(BaseClass):
    def call_me(self):
        BaseClass.call_me(self)
        print("Right")

class Sup(Left, Right):
    def call_me(self):
        Left.call_me(self)
        Right.call_me(self)
        print("Sup")


s = Sup()
s.call_me()
