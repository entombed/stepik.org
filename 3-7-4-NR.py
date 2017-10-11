from xml.etree import ElementTree
'''
str_xml = input()
root = ElementTree.fromstring(str_xml)
'''
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