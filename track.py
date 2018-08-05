from pattern import *

class Track:
    """Track definitions"""

    def __init__(self):
        self.name = "track"
        self.port = 0
        self.channel = 1
        self.patterns = []
        self.references = []

    def AddPattern(pattern):
        self.patterns.append(pattern)

    def RemovePattern(pattern):
        self.patterns.remove(pattern)

