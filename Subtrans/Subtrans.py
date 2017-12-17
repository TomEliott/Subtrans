####################
##### SUBTRANS #####
####################
##  Version 1.42  ##

# By
# Tom-Eliott Herfray (Find3r)
# Samy Hussaein (Mysa)

from Packages.srt import srt
from Packages.googletrans import googletrans
from Packages.googletrans.googletrans.client import Translator

def subtrans(filePath, src, dest):
    """Translates the SRT file from an original language <src> 
    to a destination language <dest>"""
    subtitle = Main(filePath, src, dest)
    SRTform = srt.compose(subtitle)
    return newSRT(SRTform, filePath)

def normalise(L):
    """Convert the list of elements in one string"""
    text = L[0]
    for i in range(1, len(L)):
        text += L[i]
    return text

def newSRT(sub, filePath):
    file = open(filePath, "w")
    file.write(sub)
    file.close()

def importFile(filePath):
    """Import the SRT file and convert it to a str"""
    file = open(filePath, "r")
    contentFile = file.readlines()
    one_string = normalise(contentFile)
    original_sub = list(srt.parse(one_string))
    file.close()
    return original_sub

def Main(filePath, source_language, dest_language):
    """Main function that returns the translated subtitle"""
    original_sub = importFile(filePath)
    L_original = srt_to_list(original_sub)
    L_new = translate(L_original, source_language, dest_language)
    new_sub = list_to_srt(L_new, original_sub)
    return new_sub

def Print(sub):
    """Show subtitles"""
    print(srt.compose(sub))
    
def srt_to_list(sub):
    """Transfer the phrases from the SRT file to a list"""
    L = []
    for i in range(len(sub)):
        text = sub[i].content
        L.append(text)
    return L

def list_to_srt(L, sub):
    """Transfer sentences from a list to an SRT file"""
    if len(L) == len(sub):
        for i in range(len(L)):
            sub[i].content = L[i]
    return sub

def translate(L, source_language, dest_language):
    """Translate the elements of the list"""
    newL = []
    translator = Translator()
    translations = translator.translate(L, dest=dest_language, src = source_language)
    for translation in translations:
        newL.append(translation.text)
    return newL