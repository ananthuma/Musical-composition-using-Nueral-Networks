from PyQt4 import QtGui,QtCore

import sys,os,cmd # We need sys so that we can pass argv to QApplication

import inter # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer
import pyaudio  
import wave,sys  



class ExampleApp(QtGui.QMainWindow, inter.Ui_Dialog):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
form = ExampleApp()  
selectedFile =  '';
playFilesrc =  '';
from pydub import AudioSegment
import subprocess
def cmpFiles():
    import subprocess,sys
    p=subprocess.Popen('musly -N;musly -a '+str(selectedFile)+';musly -a '+str(selectFile()),shell='True',stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print p.stdout.read()
    p=subprocess.Popen('musly -m out.txt',shell='True',stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print p.stdout.read()
    p=subprocess.Popen('cat out.txt|tail -1',shell='True',stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    #print p.stdout.read().split('    ')[1].split('  ')[0]
    form.label.setText(p.stdout.read().split('\t')[1])
    form.pushButton_3.setText(str(p.stdout.read().split('\t')[1]) )
def mergeFiles():
    sound1 = AudioSegment.from_file(str(selectedFile));
    sound2 = AudioSegment.from_file(str(selectFile()));

    combined = sound1.overlay(sound2)

    combined.export("combined.wav", format='wav')
    global playFilesrc;
    playFilesrc=QtCore.QString("combined.wav")
def playFile():
    chunk = 2048  
    print  playFilesrc
    if(playFilesrc):
        f = wave.open(str(playFilesrc),"rb") 
        p = pyaudio.PyAudio()   
        
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
        data = f.readframes(chunk)  
        form.label.setText(QtCore.QString("Playing.."))
        while data != '':  
            stream.write(data)  
            data = f.readframes(chunk)  
        stream.stop_stream()  
        form.label.setText(QtCore.QString("Stopped"))
        stream.close()    
        p.terminate()

def selectFirstFile():
    print "selectFirstFile"
    global selectedFile
    selectedFile=selectFile()
    global playFilesrc
    playFilesrc=selectedFile
    form.label_5.setText(selectedFile)
def quitClicked(self):
    
    QtCore.QCoreApplication.instance().quit()

def selectFile():
    print "selectfile"
    return QtGui.QFileDialog.getOpenFileName()
def main():
    form.pushButton_2.clicked.connect(playFile)
    form.pushButton_3.clicked.connect(cmpFiles)
    form.pushButton_4.clicked.connect(mergeFiles)
    form.pushButton.clicked.connect(selectFirstFile) 
    form.pushButton_5.clicked.connect(quitClicked)       # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app
    

if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
