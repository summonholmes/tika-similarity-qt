# Tika-Similarity-Qt
A simple front-end for [Tika-Similarity](https://github.com/chrismattmann/tika-similarity) in PyQt4 and/or PyQt5.

![alt text](https://raw.githubusercontent.com/summonholmes/tika-similarity-qt4/master/Example_2.png)

Pre-requisites
===
[Tika-Similarity](https://github.com/chrismattmann/tika-similarity)  

Dependencies
===
python2.7  
python-cluster  
python-editdistance  
python-jellyfish  
python-nltk  
python-nltk-punkt  
python-nltk-averaged_perceptron_tagger  
python-porter  
python-requests  
python-scipy  
python-stemming  
python-tika  
qt4   /   qt5  
pyqt4   /   pyqt5  

Installation (Just an example!)
===
Linux/Unix  
1. Clone [Tika-Similarity](https://github.com/chrismattmann/tika-similarity) to your home folder.
```
$ git clone https://github.com/chrismattmann/tika-similarity
```
2. Clone this repository [Tika-Similarity-Qt](https://github.com/summonholmes/tika-similarity-qt) to your home folder.
```
$ git clone https://github.com/summonholmes/tika-similarity-qt
```
3. Run:

```
$ mv ~/tika-similarity-qt4/tika-similarity-qt4-unix-linux.py ~/tika-similarity/

$ chmod +x ~/tika-similarity/tika-similarity-qt4-unix-linux.py && ~/tika-similarity/tika-similarity-qt4-unix-linux.py
OR
$ python2.7 ~/tika-similarity/tika-similarity-qt4-unix-linux.py
```   

Windows
1. Clone or download & extract [Tika-Similarity](https://github.com/chrismattmann/tika-similarity) to your home folder.  
2. Clone this repository [Tika-Similarity-Qt](https://github.com/summonholmes/tika-similarity-qt) to your home folder. 
3. Drag the tika-similarity-qt4-windows.py file from the 'tika-similarity-qt' folder into the 'tika-similarity' folder.
3. Run:
```
C:\Python27\python.exe %USERPROFILE%/tika-similarity/tika-similarity-qt4-windows.py
```  
The only difference in the Windows version is the substitution of '~' with '%USERPROFILE%' and 'python2' with 'C:\Python27\python.exe'  

* You may susbstitute 'tika-similarity-qt4.py' with 'tika-similarity-qt5.py' for either of the above installations, or use both.

Windows requires manually updating the PATH environmental variable if the user chooses to use the command line often, so the path to the full python executable is included instead.  

Windows users may also obtain a PyQt4 installer from the Sourceforge pages at https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/.  Remember to choose Python version 2.7 and the correct version of the installed Python system architecture (could be x32 on a x64 system).  

For PyQt5 on Windows, you must build PyQt5 against Python 2.7 because there are only installers for Python 3.x. https://sourceforge.net/projects/pyqt/files/PyQt5/. 


License
===

This project is licensed under the [Apache License, version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

Questions, Comments, etc?
===
Email me [Shane Kimble](mailto:shanekimble12@hotmail.com).
