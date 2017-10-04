import os
import os.path
with open('rez.txt', 'w') as rezFile:
    for currentDir, dirs, files in os.walk('main'):
        for tmpFile in files:
            if tmpFile.endswith('.py'):
                rezFile.write(currentDir)
                rezFile.write('\n')
                break
