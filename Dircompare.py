#playing around with python
#eventually will create a file and list of the directories

import sys
import os


#main function
def main():

    """var = raw_input("Enter direcotry to scan: ").rstrip('\n')
    print var

    for filename in os.listdir(var):
        print filename"""

    setFiledata()

    

#function to read in files and create output to file
def setFiledata():

    """ working code, just want to comment out so I don't have to maunally
    enter in the data each time will still creating this.
    #ask for dir for file to read from
    fdir = raw_input("Enter directory to check: ")

    #check if dir exists if not exit
    if os.path.exists(fdir):
        print("Path exists")
    else:
        print ("path does not exist")
        return
    """

    #get a name to set file
    fname = raw_input("Save file name?: ").rstrip('\n')
    
    #checks if a file exists if is does not creates it
    if os.path.exists(fname + ".txt"):
        print("file name already exists overwriting")
        f = file(fname + ".txt", "r+")
    else:
        f = file(fname + ".txt", "w")
            

    #temp set of dir so I don't have to enter it every time
    fdir = "C:\\Python27\\Test"

    #function to map out save file for direcotry
    dSearch(fdir, f)

    #function compare files
    #using premade data for checking.
    filetemp1 = file("test.txt", "r+")
    filetemp2 = file("test1.txt", "r+")
    dCompare(filetemp1, filetemp2)

        
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
        #output debug info to make sure working correctly
        #TODO possible add complete filepath for easier checking of files (later)
        if os.path.isdir(filename):
            #if folder set name and value to -1 to mark as a folder
            #call the function again with the value set to 1 to skip initial checks
            print("is a folder\n")
            fsave.write(filename + "\n")
            fsave.write("-1\n")
            dSearch(filedir + "\\" + filename, fsave)
        else:
            print("is a file\n")
            #Set the file name on one line and the file size on a different
            #line inside a file for easier reading
            fsave.write(filename + "\n")
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
    else:
        print "files are different"

#TODO add a gui
#TODO maybe display where files are different

    
#standard to call main function 
if __name__ == '__main__':
    main()
    
