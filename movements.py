from node import Node


def firstJarFilled(currentNode):
    newNode = Node(currentNode.firstJar, currentNode.secondJar, currentNode.firstJar,
                   currentNode.secondJarCurrentVolume, currentNode, currentNode.treeLevel + 1)
    return newNode


def secondJarFilled(currentNode):
    newNode = Node(currentNode.firstJar, currentNode.secondJar,currentNode.firstJarCurrentVolume,
                   currentNode.secondJar, currentNode, currentNode.treeLevel + 1)
    return newNode


def firstJarEmpty(currentNode):
    newNode = Node(currentNode.firstJar, currentNode.secondJar, 0,
                   currentNode.secondJarCurrentVolume, currentNode, currentNode.treeLevel + 1)
    return newNode


def secondJarEmpty(currentNode):
    newNode = Node(currentNode.firstJar, currentNode.secondJar, currentNode.firstJarCurrentVolume,
                   0, currentNode, currentNode.treeLevel + 1)
    return newNode


def fillFirstJarWithSecondJar(currentNode):
    value = currentNode.firstJarCurrentVolume + currentNode.secondJar
    if value > currentNode.firstJar:
        value = currentNode.firstJar
    newNode = Node(currentNode.firstJar, currentNode.secondJar, value,
                   0, currentNode, currentNode.treeLevel + 1)
    return newNode
    # if currentNode.firstJarCurrentVolume == 0
    #     value = currentNode.secondJar
    # elif value > currentNode.firstJar:
    #     value = currentNode.firstJar


def fillSecondJarWithFirstJar(currentNode):
    value = currentNode.secondJarCurrentVolume + currentNode.firstJar
    if value > currentNode.secondJar:
        value = currentNode.secondJar
    newNode = Node(currentNode.firstJar, currentNode.secondJar, 0,
                   value, currentNode, currentNode.treeLevel + 1)
    return newNode


def emptySecondJarInFirstJar(currentNode):
    value = currentNode.firstJarCurrentVolume + currentNode.secondJarCurrentVolume
    if value > currentNode.firstJar:
        value = currentNode.firstJar
    newNode = Node(currentNode.firstJar, currentNode.secondJar, value,
                   0, currentNode, currentNode.treeLevel + 1)
    return newNode

def emptyFirstJarInFirstJar(currentNode):
    value = currentNode.secondJarCurrentVolume + currentNode.firstJarCurrentVolume
    if value > currentNode.secondJar:
        value = currentNode.secondJar
    newNode = Node(currentNode.firstJar, currentNode.secondJar, 0,
                   value, currentNode, currentNode.treeLevel + 1)
    return newNode
