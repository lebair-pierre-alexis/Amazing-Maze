def readFile(fileName):
    file = open(fileName, "rt")
    text = file.read()
    file.close()
    return text

def writeFile(fileName, content):
    file = open(fileName, "wt")
    file.write(content)
    file.close