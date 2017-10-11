def check(cls, par):
    global found
    if cls in myDict[par]:
        found = 1
        return found
    else:
        for i in myDict[par]:
            check(i, par)

'''
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
print(myDict)
'''
myDict = {'A': ['A'], 'B': ['A'], 'C': ['A'], 'D': ['B', 'C']}
found = 0
print (check('A','D'))
'''
4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
'''