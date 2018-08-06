from note import *

class ID:
    """Identification"""

    def __init__(self):
        self.letter = 0
        self.digit = 0

class Pattern(ID):
    """Pattern definition"""

    def __init__(self):
        self.notes = []

    def addNote(note):
        self.notes.append(note)

    def removeNote(note):
        self.notes.remove(note)
        
class Reference(ID):
    """Reference definition"""

    def __init__(self):
        self.bar = 0
        
