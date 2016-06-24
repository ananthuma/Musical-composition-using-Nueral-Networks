from PyQt4 import QtGui,QtCore
import uitrain,sys
class ExampleApp(QtGui.QMainWindow, uitrain.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in ui.py file automatically
                            # It sets up layout and widgets that are defined
app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
form = ExampleApp()  
def main():
    #form.folderBtn.clicked.connect(selectFolder)
  
    form.show()                         # Show the form
    app.exec_() 

if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
