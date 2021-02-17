from chord_type import ChordType


class PChord:
    c_seq = list

    def __init__(self, index: int, type: ChordType):
        self.index = index - 1
        self.type = type
        self.generateSeq()

    def generateSeq(self):
        if self.type == ChordType.maj:
            self.c_seq = [0, 4, 7]
        elif self.type == ChordType.min:
            self.c_seq = [0, 3, 7]
        elif self.type == ChordType.maj7:
            self.c_seq = [0, 3, 7, 10]
        elif self.type == ChordType.sus2:
            self.c_seq = [0, 2, 7]
        elif self.type == ChordType.sus4:
            self.c_seq = [0, 5, 7]
