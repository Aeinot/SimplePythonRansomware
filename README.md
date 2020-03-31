# SimplePythonRansomware

Test de développement d'un ransomware en Python pour Windows. 

## Requirements

### pyAesCrypt 

```bash
pip3 install pyAesCrypt
```

### auto-py-to-exe

Ce package permet de convertir le script python en fichier exécutable. Il ne fonctionne pas bien sous Python 3.8, il est donc suggéré de créer un environnement virtuel avec Python 3.7 :

```bash
# Création de l'environnement virtuel
c:\path\to\Python\Python37\python.exe -m venv c:\path\to\myenv
# Activation
c:\path\to\myenv\Scripts\activate.bat
# Installation de pyAesCrypt
pip3 install pyAesCrypt
# Installation de auto-py-to-exe
pip3 install auto-py-to-exe
# Lancement de auto-py-to-exe
python -m auto_py_to_exe
```



## Usage

#### Chiffrement

Le script permet de chiffrer tous les fichiers contenus dans le dossier `IMPORTANT` situé à la racine du dossier de l'utilisateur courant (`%HOMEPATH%\IMPORTANT\`). Pour cela, il suffit de double cliquer sur l'exécutable, ou de lancer le script sans arguments :

```bash
# Exécution du script python
python3 ransomware.py
# Exécution du .exe
ransomware.exe
```

Le ransomware écrira la clé de chiffrement dans le fichier `ransomware_key.txt`

#### Déchiffrement

```bash
# Exécution du script python
python3 ransomware.py -d ransomware_key.txt
# Exécution du .exe
ransomware.exe -d ransomware_key.txt
```





