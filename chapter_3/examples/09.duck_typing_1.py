class FlacFile:
    def __init__(self, filename):
        self.filename = filename

    def play(self):
        print(f"palying {self.filename} as flac")


flac = FlacFile("song.flac")
flac.play()
