''' 
https://stepik.org/lesson/24460/step/9?unit=6766

'''
myDict = {'global':{'parent': None, 'vars':[]}}

def create (namespace, parent):
    global myDict
    myDict.update({namespace:{'parent':parent, 'vars':[]}})

def add (namespace, var):
    global myDict
    myDict[namespace]['vars'].append(var)

def get (namespace, var):
    #obj = namespace
    while (True):
        if var in myDict[namespace]['vars']:
            print(namespace)
            break
        elif namespace == 'global':
            print(myDict[namespace]['parent'])
            break
        else:
            namespace = myDict[namespace]['parent']
count = int(input())
for i in range(count):
    f, n, v = input().split()
    if f == 'add':
        add(n, v)
    elif f == 'create':
        create(n, v)
    elif f == 'get':
        get(n, v)