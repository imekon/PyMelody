import track as pytrack

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
        track = pytrack.Track()
        track.name = name
        track.channel = channel
        self.tracks.append(track)
        return track
