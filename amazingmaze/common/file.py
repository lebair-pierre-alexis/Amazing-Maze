def readFile(fileName):
    file = open(fileName, "rt")
    text = file.read()
    file.close()
    return text

def writeFile(fileName, content, mode):
    if fileName == "":
        fileName = input("Entrez le nom du fichier dans lequel enregistrer le labyrinthe (doit finir par .mz.txt) : ")
    file = open(fileName, mode)
    file.write(content)
    file.close