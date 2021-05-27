class NodePath:
    def __init__(self, firstPos, secondPos, thirdPos):
        self.firstPos = firstPos
        self.secondPos = secondPos
        self.thirdPos = thirdPos

    def __str__(self) -> str:
        return "{}, {}, {}".format(self.firstPos, self.secondPos, self.thirdPos)

