from track import *

class Song:
    """Song definition"""

    def __init__(self):
        self.name = "untitled"
        self.ppqn = 96
        self.tempo = 120
        self.tracks = []

        self.CreateTrack("Lead", 1)
        self.CreateTrack("Pad", 4)
        self.CreateTrack("Bass", 7)
        self.CreateTrack("Drums", 10)

    def CreateTrack(self, name, channel):
        track = Track()
        track.name = name
        track.channel = channel
        self.tracks.append(track)
        return track

    def FindTrack(self, channel):
        for track in self.tracks:
            if track.channel == channel:
                return track

        return None

    def Import(self, filename):
        pass

    def Export(self, filename):
        pass
