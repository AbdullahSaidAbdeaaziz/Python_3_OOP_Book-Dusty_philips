class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        print(f"playing {self.filename} as mp3")

class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print(f"playing {self.filename} as wav")


files = [MP3File("song.mp3"), WavFile("sound.wav")]
for file in files:
    file.play()


# MP3File("song.wav") # output: error(Invalid file format)
