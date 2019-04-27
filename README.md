
# Subtrans
<<<<<<< HEAD
[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)](https://www.python.org) [![FocalStudio](https://img.shields.io/badge/Powered%20by-Focal%20Studio-lightgrey.svg)](https://www.focalstudio.me)
=======
[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)](https://www.python.org) [![FocalStudio](https://img.shields.io/badge/Powered%20by-Focal%20Studio-lightgrey.svg)](http://focalstudio.me)
>>>>>>> 9c218276d6caeb9ad19dfae84c26de166e15ee12
----------

## What is Subtrans?

**Subtrans** is a simple Python program that translates an *SRT* subtitle file from an original language to a destination language, keeping the same specificities. The program uses the `Googletrans` and `SRT` libraries to translate the file, and requires an internet connection to connect to the *Google API*.

*Note : Google Translation's API has evolved, so it's possible that the program hangs at any time, I'm working on a new version using the [*Deepl's API*](https://www.deepl.com/fr/docs-api.html).* 

### Installation
```shell
pip install -U git+https://github.com/TomEliott/Subtrans.git@develop
```

Or download the [Subtrans Package](https://github.com/TomEliott/Subtrans/archive/master.zip).

### Utilisation
Use the command below, with `filePath` the path of the SRT file, `src` the original language and `dest` the destination language.

```shell
$ python subtrans.py <filePath> <src> <dest>
```

> Example : `python subtrans.py 'AvengersEndgame.srt' 'en' 'fr'"`

*Note : For the list of available languages, please consult the [*Google Translate*](https://translate.google.com/intl/en/about/languages) database and use the [*ISO 3166-2*](https://en.wikipedia.org/wiki/ISO_3166-2) form for the language format.*

### Credits

**Tom-Eliott `'Find3r'`** [(GitHub)](https://github.com/TomEliott) & **Samy `'Mysa'`** [(GitHub)](https://github.com/SamyHussaein)
