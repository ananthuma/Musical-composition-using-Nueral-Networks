from PyQt4 import QtGui,QtCore
import sys,os,cmd 
from os import listdir
from os.path import isfile,join
import ui # This file holds our MainWindow and all design related things
import pyaudio  
import wave,sys 
class ExampleApp(QtGui.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in ui.py file automatically
                            # It sets up layout and widgets that are defined

app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
form = ExampleApp()  
filearray  =[];
filesInFolder=[];
selectedFiles=[];
play= True;
from pydub import AudioSegment
import subprocess
def mergeFiles():
    #sound1 = AudioSegment.from_file(str(selectedFile));
    #sound2 = AudioSegment.from_file(str(selectFile()));
	#combined = sound1.overlay(sound2)
	i=0;
	while(i<len(selectedFiles)-1):
 		sound = AudioSegment.from_file(str(selectedFiles[0]));
 		i=i+1;
 		sound2 = AudioSegment.from_file(str(selectedFiles[i]));
 		if(i==1):
 			combined = sound.overlay(sound2);
 		else:
 			combined = combined.overlay(sound2);
 		
	combined.export("combined.wav", format='wav')
import subprocess,sys  
def cmpFiles():
    
    p=subprocess.Popen('musly -N',shell='True',stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    for f in selectedFiles:
		p=subprocess.Popen('musly -a '+str(f),shell='True',stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		print p.stdout.read()
    p=subprocess.Popen('musly -m out.txt',shell='True',stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print p.stdout.read()
    p=subprocess.Popen('cat out.txt',shell='True',stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    #print p.stdout.read().split('    ')[1].split('  ')[0]
    form.outputView.setText(p.stdout.read())
    #form.pushButton_3.setText(str(p.stdout.read().split('\t')[1]) )  

def selectFolder():
	folderPath = str(QtGui.QFileDialog.getExistingDirectory())
	print folderPath;
	#filesInFolder= [f for f in listdir(folderPath) if  isfile(join(folderPath,f))f.endswith(".wav")]
	for f in listdir(folderPath):
		if(f.endswith(".wav")):
			filesInFolder.append(f);

	print filesInFolder

	form.filelistWidget.insertItems(len(filesInFolder),filesInFolder)

def addFile():
	selectedFiles.append(str(form.filelistWidget.currentItem().text()));
	form.Seletedlist.clear();
	form.Seletedlist.insertItems(len(selectedFiles),selectedFiles)	
	
def playFile():
    chunk = 2048  
    form.filelistWidget.currentItem().text()
    global play
    play=True
    if(True):
    	print  str(form.filelistWidget.currentItem().text())
        f = wave.open(str(form.filelistWidget.currentItem().text()	),"rb") 
        p = pyaudio.PyAudio()   
        
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
        data = f.readframes(chunk)  
        
        while data != '':  
            stream.write(data)  
            data = f.readframes(chunk) 
            if(play==False):
            	break;
        
       	stream.stop_stream()  
        	
        stream.close()    
        p.terminate()

def clearList():
	form.Seletedlist.clear();
	global selectedFiles
	selectedFiles=[]

def stop():
	global play
	play = False;
def main():
    form.folderBtn.clicked.connect(selectFolder)
    form.playButton.clicked.connect(playFile)
    form.addBtn.clicked.connect(addFile)
    form.MergeBtn.clicked.connect(mergeFiles)
    form.compareBtn.clicked.connect(cmpFiles)
    form.pushButton.clicked.connect(clearList)
    form.stop.clicked.connect(stop)
    form.show()                         # Show the form
    app.exec_() 

if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
