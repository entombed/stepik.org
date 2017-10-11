'''
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.
Ценность цвета равна сумме ценностей всех кубиков этого цвета.
Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
Sample Input:
<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
Sample Output:
4 3 1
'''
from xml.etree import ElementTree

def getChild(root, lvl):
    global rezDict
    lvl += 1
    rezDict[root.attrib['color']] += lvl
    for child in root:
        if child.getchildren():
            getChild(child, lvl)
        else:
            lvl += 1
            rezDict[child.attrib['color']] += lvl
            lvl -= 1

rezDict = {'green':0, 'red':0, 'blue':0}
xmlFile = input()
#tree = ElementTree.parse(xmlFile)
tree = ElementTree.fromstring(xmlFile)
#root = tree.getroot()
root = tree
lvl = 0
getChild(root, lvl)
print('{} {} {}'.format(rezDict['red'],rezDict['green'],rezDict['blue']))
'''
blue-1 1
red2-1 2
green3-1 3
red-3-2 3
red4-1 4
blue4-2 4
blue4-3 4
red2-2 2
'''