from Program import Subtrans

def Translate_a_subtitle(filePath, src, dest):
	"""
	Translates the same file given as a parameter <filePath> 
	from the original language <src> to the destination language <dest>
	"""
	return Subtrans.subtrans(filePath, src, dest)