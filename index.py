from node import Node
from movements import *

firstJarrVolume = 4
secondJarVolume = 3
finalVolume = 2
limit = 17


def exploreTree():
    stack = []
    path = []
    wasFound = False
    startingNode = Node(firstJarrVolume, secondJarVolume, firstJarrVolume, secondJarVolume)
    stack.append(startingNode)
    while (wasFound != True) and (len(stack) > 0):
        temporalNode = stack.pop()
        print("actual")
        print(temporalNode.getValues())
        temporalTreeLevel = temporalNode.treeLevel
        # temporalFather = temporalNode.nodeFather
        firstJarFilledNode = firstJarFilled(temporalNode)
        secondJarFilledNode = secondJarFilled(temporalNode)
        firstJarEmptyNode = firstJarEmpty(temporalNode)
        secondJarEmptyNode = secondJarEmpty(temporalNode)
        fillFirstJarWithSecondJarNode = fillFirstJarWithSecondJar(temporalNode)
        fillSecondJarWithFirstJarNode = fillSecondJarWithFirstJar(temporalNode)
        emptySecondJarInFirstJarNode = emptySecondJarInFirstJar(temporalNode)
        emptyFirstJarInFirstJarNode = emptyFirstJarInFirstJar(temporalNode)
        if temporalNode.totalVolume == finalVolume:
            print("Respuesta encontrada")
            wasFound = True
            limit = temporalNode.level - 1
            showPath(temporalNode)
            break
        elif temporalNode.treeLevel + 1 < 17:
            if temporalNode.secondJar != temporalNode.secondJarCurrentVolume and path.count(
                    secondJarFilledNode.getValues()) == 0:
                print("segunda")
                print (temporalTreeLevel)
                print(secondJarFilledNode.getValues())
                stack.append(secondJarFilledNode)
                path.append(secondJarFilledNode.getValues())
            if temporalNode.firstJarCurrentVolume != 0 and path.count(
                    firstJarEmptyNode.getValues()) == 0:
                print ("tercera")
                print (temporalTreeLevel)
                print(firstJarEmptyNode.getValues())
                stack.append(firstJarEmptyNode)
                path.append(firstJarEmptyNode.getValues())
            if temporalNode.secondJarCurrentVolume != 0 and path.count(
                    secondJarEmptyNode.getValues()) == 0:
                print ("cuarta")
                print (temporalTreeLevel)
                print(secondJarEmptyNode.getValues())
                stack.append(secondJarEmptyNode)
                path.append(secondJarEmptyNode.getValues())
            if temporalNode.firstJar != temporalNode.firstJarCurrentVolume and path.count(
                    firstJarFilledNode.getValues()) == 0:
                print("primera")
                print (temporalTreeLevel)
                print(firstJarFilledNode.getValues())
                stack.append(firstJarFilledNode)
                path.append(firstJarFilledNode.getValues())
            if path.count(fillFirstJarWithSecondJarNode.getValues()) == 0:
                print("lo demas")
                print (temporalTreeLevel)
                print(fillFirstJarWithSecondJarNode.getValues())
            if path.count(firstJarFilledNode.getValues()) == 0:
                print(fillSecondJarWithFirstJarNode.getValues())
                stack.append(fillFirstJarWithSecondJarNode)
            if :
                print(emptySecondJarInFirstJarNode.getValues())
                stack.append(fillSecondJarWithFirstJarNode)
                print(emptyFirstJarInFirstJarNode.getValues())

                stack.append(emptySecondJarInFirstJarNode)
                stack.append(emptyFirstJarInFirstJarNode)
        else:
            print ("No encontrado")
            break


def showPath(resul):
    while (resul.nodeFather != None):
        print(resul.nodeFather.getValues())
        resul = resul.nodeFather
        pass


exploreTree()
