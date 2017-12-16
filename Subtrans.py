######################
###### SUBTRANS ######
######################
## Version 1.0
## By Find3r & Mysa

import pip

### Exemple
original_sub = list(srt.parse('''\
... 1
... 00:00:33,843 --> 00:00:38,097
... My name is Barry Allen
...
... 2
... 00:00:40,641 --> 00:00:44,687
... I'm the fastest men alive
...
... 3
... 00:00:57,908 --> 00:01:03,414
... And I'm also the Flash
...
... '''))



### Fonctions de réglages
def install(package):
    pip.main(['install', package])

def mainInstall():
    """UNIQUEMEMENT si c'est la première fois que vous l'utilisez"""
    install('-U srt')
    install('-U git+https://github.com/cdown/srt.git@develop')
    install('googletrans')
    install('pysrt')
    importIndex()
    
def importIndex():
    """À lancer à chaque utilisation"""
    import srt
    import pysrt
    from googletrans import Translator
    
    

### Fonctions de manipulation des listes
def importFile(filePath, language): ## TO FIX avec la librairie SRT et NON PYSTR
    """Importe le fichier SRT et spécifie la langue d'origine"""
    file = pysrt.open(filePath)#fix
    original_sub = list(srt.parse('''file ''')) #faut import du texte
    return (original_sub, language)
    
def srt_to_list(sub): #ok
    """Transfère les phrases du srt dans une liste"""
    L = []
    for i in range(len(sub)):
        text = sub[i].content
        L.append(text)
    return L

def list_to_srt(L, sub): #ok
    """Remplace les phrases d'une liste dans le srt"""
    if len(L) == len(sub):
        for i in range(len(L)):
            sub[i].content = L[i]
    return sub
    

### Fonctions de traduction
def translate(L, source_language, dest_language): #ok
    """Traduit les élements de la liste"""
    newL = []
    translator = Translator()
    translations = translator.translate(L, dest=dest_language, src = source_language)
    for translation in translations:
        newL.append(translation.text)
    return newL
    
    
### TESTBOX
original_L = srt_to_list(original_sub)
new_L = translate(L, 'en', 'fr')
new_sub = list_to_srt(new_L, original_sub)
print(srt.compose(new_sub))