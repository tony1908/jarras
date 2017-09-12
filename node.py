class Node():
    def __init__(self, firstPitcher, secondPitcher, firstJarCurrentVolume,
                 secondJarCurrentVolume, nodeFather=None, treeLevel=0):
        self.firstJar = firstPitcher
        self.secondJar = secondPitcher
        self.nodeFather = nodeFather
        self.treeLevel = treeLevel
        self.firstJarCurrentVolume = firstJarCurrentVolume
        self.secondJarCurrentVolume = secondJarCurrentVolume

    def totalVolume(self):
        return self.firstJarCurrentVolume + self.secondJarCurrentVolume

    def getValues(self):
        return [self.firstJarCurrentVolume, self.secondJarCurrentVolume]
