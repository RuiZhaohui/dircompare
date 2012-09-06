#playing around with python
#eventually will create a file and list of the directories

import sys
from PyQt4 import QtGui, QtCore
import os
import datetime

#main function
def main():

    app = QtGui.QApplication(sys.argv)

    mw = mWindow()   
    sys.exit(app.exec_())

#function to read in files and create output to file
def setFiledata(fdir, filename):

    now = datetime.datetime.now()
    
    #get a name to set file    
    fname = filename
    
    #checks if a file exists if is does not creates it
    if os.path.exists(fname + ".txt"):
        print("file name already exists overwriting")
        f = file(fname + ".txt", "r+")
    else:
        f = file(fname + ".txt", "w")
            

    #function to map out save file for direcotry
    dSearch(fdir, f)    

        
#function to check directory for files
#recursive
def dSearch(filedir, fsave):
    print "in dSearch"
    
    #prints out size of file in an easier to read format
    for filename in os.listdir(filedir):
        print filename
        filesize = os.path.getsize(filedir + "//" + filename)

        #output filesize in easier to read format then bytes
        if filesize >= 1048576:
            print str(filesize / 1048576) + " MB" 
        elif filesize >= 1024:
            print str(filesize /1024) + "kb"
        else:
            print str(filesize) + "b"


        #check if the current file is a directory of file
        #TODO possible add complete filepath for easier checking of files (later)
        if os.path.isdir(filename):
            #if folder set name and value to -1 to mark as a folder
            #call the function again with the value set to 1 to skip initial checks
            fsave.write(filedir + "\\" + filename + "\n")
            fsave.write("-1\n")
            dSearch(filedir + "\\" + filename, fsave)
        else:
            #Set the file name on one line and the file size on a different
            #line inside a file for easier reading
            fsave.write(filedir + "\\" + filename + "\n")
            fsave.write(str(filesize) + "\n")


#fucntion to compare files
def dCompare(newfile, oldfile):
    print "in dCompare"

    #create a file to set compared data to
    print("results being saved to Results.txt\n")
    if os.path.exists("Results.txt"):
        print("file results already exists overwriting\n")
        f = file("Results.txt", "r+")
    else:
        f = file("Results.txt", "w")

    newfilelist = []
    oldfilelist = []
    #grab both files into an array
    for line in newfile:
        newfilelist.append(line)
    for line in oldfile:
        oldfilelist.append(line)
        
    #run the old file to the new file and check for differences
    if newfilelist == oldfilelist:
        print "files are the same"
        return True
    else:
        print "files are different"
        return False

#TODO add a gui
#TODO maybe display where files are different

class mWindow(QtGui.QWidget):

    def __init__(self):
        super(mWindow, self).__init__()

        self.initUI()

    def initUI(self):            
        
        self.setGeometry(600, 600, 300, 300)
        self.setWindowTitle('Directory Compare')
       
        #labels
        ScanDir              = QtGui.QLabel('Scan directory:', self)
        self.ScanDirLocation = QtGui.QLabel('                ', self)
        SaveL                = QtGui.QLabel('Save Name:', self)
        BoxBreak             = QtGui.QLabel('----------------------------------------------------------------------', self)
        Compare1             = QtGui.QLabel('Compare file1:', self)
        Compare2             = QtGui.QLabel('Compare file2:', self)
        self.Compare1dir     = QtGui.QLabel('                                            ', self)
        self.Compare2dir     = QtGui.QLabel('                                            ', self)
        self.Results         = QtGui.QLabel('                                     ', self)
        
        ScanDir.move(10, 15)
        self.ScanDirLocation.move (90, 15)
        SaveL.move(10,40)
        BoxBreak.move(10, 100)
        Compare1.move(10, 120)
        Compare2.move(10, 150)
        self.Compare1dir.move(85, 120)
        self.Compare2dir.move(85, 150)
        self.Results.move(110, 225)

        #input field
        self.inputfield = QtGui.QLineEdit(self)
        self.inputfield.move(70, 37)

        #buttons
        ScanDirB   = QtGui.QPushButton('Select', self)
        ScanSaveB  = QtGui.QPushButton('Save', self)
        CheckDirB  = QtGui.QPushButton('Select', self)
        CheckDirB2 = QtGui.QPushButton('select', self)
        CompareB   = QtGui.QPushButton('Compare', self)

        ScanDirB.move(220, 12)
        ScanSaveB.move(110, 65)
        CheckDirB.move(220, 115)
        CheckDirB2.move(220, 145)
        CompareB.move(110, 180)
        
        ScanDirB.clicked.connect(self.scanButtonClicked)
        ScanSaveB.clicked.connect(self.SaveDirButtonClicked)
        CheckDirB.clicked.connect(self.CheckDirButton1Clicked)
        CheckDirB2.clicked.connect(self.CheckDirButton2Clicked)
        CompareB.clicked.connect(self.CompareButtonClicked)


        #display all
        self.show()

    def scanButtonClicked(self):
        lbl = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ScanDirLocation.setText(lbl)

    def SaveDirButtonClicked(self):
        setFiledata(self.ScanDirLocation, self.inputfield.text())

    def CheckDirButton1Clicked(self):
        lbl = str(QtGui.QFileDialog.getOpenFileName(self, "Open text file", "", self.tr("Text Files (*.txt)")))
        self.Compare1dir.setText(lbl)

    def CheckDirButton2Clicked(self):
        lbl = str(QtGui.QFileDialog.getOpenFileName(self, "Open text file", "", self.tr("Text Files (*.txt)")))
        self.Compare2dir.setText(lbl)

    def CompareButtonClicked(self):
        if dCompare(self.Compare1dir.text(), self.Compare2dir.text()):
            self.Results.setText("Files are the same")
        else:
            self.Results.setText("Files are different")
        
        
            
#standard to call main function 
if __name__ == '__main__':
    main()
    
