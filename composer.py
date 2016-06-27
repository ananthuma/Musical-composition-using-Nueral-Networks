from PyQt4 import QtGui,QtCore
import uicomp,sys,comp
tunes=['c','c#','d','d#','e','f','f#','g','g#','a','a#','b','r','c#','d','d#','e','f','f#','g','g#','a','a#']
def convertNotesToInt(note):
	if(note in tunes):
		return tunes.index(note);
	else:
		print "Error converting ",note
class ExampleApp(QtGui.QMainWindow, uicomp.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in ui.py file automatically
                            # It sets up layout and widgets that are defined
app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
form = ExampleApp() 
starting_notes=[0,0,0,0,0,0,0,0]
def compose():
	starting_notes[0]=convertNotesToInt(form.note1_2.toPlainText())
	starting_notes[1]=convertNotesToInt(form.note2_2.toPlainText())
	starting_notes[2]=convertNotesToInt(form.note3_2.toPlainText())
	starting_notes[3]=convertNotesToInt(form.note4_2.toPlainText())
	filename=str(form.lineEdit.text())
	if(form.sree.isChecked()):
		selectedraga=1;
	elif(form.sankar.isChecked()):
		selectedraga=2;
	elif(form.maya.isChecked()):
		selectedraga=3;
	else:
		selectedraga=4;
	
	bpm=int(form.tempo.text())
	print starting_notes,filename
	txt= comp.composer("filename",starting_notes,bpm,selectedraga,filename)
	
def main():
    form.composeBtn.clicked.connect(compose)
   
    form.show()                         # Show the form
    app.exec_() 

if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
