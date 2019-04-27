from Program import Subtrans
import sys

def Translate_a_subtitle(filePath, src, dest):
	"""
	Translates the same file given as a parameter <filePath> 
	from the original language <src> to the destination language <dest>
	"""
	return Subtrans.subtrans(filePath, src, dest)

if (len(sys.argv) == 1 or len(sys.argv) > 4):
	print("Please use the following command : python subtrans.py <filepath> <language source> <language destination>")
else:
	PATH = sys.argv[1]
	SRC = sys.argv[2]
	DEST = sys.argv[3]
	Translate_a_subtitle(PATH, SRC, DEST)