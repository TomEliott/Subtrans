
# Subtrans
[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)](https://www.python.org) [![FocalStudio](https://img.shields.io/badge/Powered%20by-Focal%20Studio-lightgrey.svg)](http://focalstud.io)
----------

## What is Subtrans?

**Subtrans** is a simple Python algorithm that translates an *SRT* subtitle file from an original language to a destination language, keeping the same specificities. The program uses the `Googletrans` and `SRT` libraries to translate the file, and requires an internet connection to connect to the *Google API*.

### Installation
```shell
pip install -U git+https://github.com/TomEliott/Subtrans.git@develop
```

Or download the [Subtrans GitHub Package](https://github.com/TomEliott/Subtrans/archive/master.zip) file, and open `Subtrans.py`.

### Utilisation
Open the `TryMe.py` file and run the function `Translate_a_subtitle (filePath, src, dest)`, with `filePath` the path of the SRT file, `src` the original language and `dest` the destination language.
```python
from Program import Subtrans

def Translate_a_subtitle(filePath, src, dest):
	return Subtrans.subtrans(filePath, src, dest)
```
> Example: `Translate_a_subtitle("TheLastJedi.srt", "en", "fr")`

NB: For the list of available languages, please consult the [Google Translate](https://translate.google.com/intl/en/about/languages/) database and use the *[ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)* form for the language format.

### Credits
Tom-Eliott `'Find3r'` [(GitHub)](https://github.com/TomEliott)

Samy `'Mysa'` [(GitHub)](https://github.com/SamyHussaein)
