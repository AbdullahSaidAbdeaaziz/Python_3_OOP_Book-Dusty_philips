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

class FlacFile:
    def __init__(self, filename):
        self.filename = filename

    def play(self):
        print(f"palying {self.filename} as flac")

class PNGFile:
    def __init__(self, filename):
        self.filename = filename

    def play(self):
        print(f"palying {self.filename} as png")

files = [MP3File("song.mp3"), WavFile("sound.wav"), FlacFile("song.flac"), PNGFile("song.png")]
for file in files:
    file.play()
