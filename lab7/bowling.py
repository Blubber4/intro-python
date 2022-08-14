class Frame(object):
    def __init__(self, n = 1):
        self.first = -1
        self.second = -1
        self.bowl_type = 0
        if n == 10:
            self.extra1 = 0
            self.extra2 = 0
        else:
            self.extra1 = -1
            self.extra2 = -1
        
    def setFirst(self, first):
        if first < 0 or first > 10:
            return

        if first == 10:
            self.bowl_type = 2

        self.first = first
        
    def setSecond(self, second):
        if second + self.first < 0 or second + self.first > 10 or second < 0:
            return

        if second + self.first == 10 and not self.isStrike():
            self.bowl_type = 1
        
        self.second = second

    def isSpare(self):
        if self.bowl_type == 1:
            return True
        return False

    def isStrike(self):
        if self.bowl_type == 2:
            return True
        return False

    def isLastFrame(self):
        if self.extra1 > -1:
            return True
        return False

    def setScore(self, score):
        self.score = score  # ??
        
    
class Match(object):
    def __init__(self):
        self.frames = []
        self.score_log = []  # score_log is list of frame numbers which still need scored (i.e because they are a spare or strike)
        
    def addFrame(self, frame):
        self.frames.append(frame)

    def calculateScore(self, n):  # n is the frame number to calculate for. Start from 1 not 0.
        print("t")

    def getFrame(self, n):
        print("f")
