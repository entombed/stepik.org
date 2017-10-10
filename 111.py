def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

myInt = int(input())
myDict = {}
for item in range(myInt):
    myStr = input().strip()
    x = myStr.split(' : ')
    myDict.update({x[0]:[x[0]]})
    if len(x) > 1:
        z = ''.join(x[1])
        zz = z.split()
        myDict.update({x[0]:zz})

myInt = int(input())
for item in range(myInt):
    myStr = input().strip()
    x = find_path(myDict, myStr[2], myStr[0])
    if x == None:
        print('No')
    else:
        print('Yes')