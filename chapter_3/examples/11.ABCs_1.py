import abc

class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

class Ogg(MediaLoader):
    def play(self):
        print("Playing ogg file")

class MP3File(MediaLoader):
    def play(self):
        print("Playing mp3 file")

class WavFile(MediaLoader):
    def play(self):
        print("Playing wav file")

class ErrorClass(MediaLoader):
    pass


files = [MP3File(), WavFile(), Ogg()]
for file in files:
    file.play()
 
# Error
# error = ErrorClass()
