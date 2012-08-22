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
    var = "F:\\Python27\\Test"

    #prints out size of file in an easier to read format
    for filename in os.listdir(var):
        print filename
        filesize = os.path.getsize(filename)

        #output filesize in easier to read format then bytes
        if filesize >= 1048576:
            print str(filesize / 1048576) + " MB" 
        elif filesize >= 1024:
            print str(filesize /1024) + "kb"
        else:
            print str(filesize) + "b"


        #check if the current file is a directory of file
        #output debug info to make sure working correctly
        if os.path.isdir(filename):
            #TODO if a folder jump into folder and do more checks
            print("is a folder\n")
        else:
            print("is a file\n")

        #Set the file name on one line and the file size on a different
        #line inside a file for easier reading
        f.write(filename + "\n")
        f.write(str(filesize) + "\n")
    


#fucntion to compare files
def dCompare(firstfile, secondfile):
    test = 5

    #TODO
    #create a new file to set compared data to
    #run the old file to the new file and check for differences
    #to make sure no files are missing run through the old file
    #through the new file
    



#standard to call main function 
if __name__ == '__main__':
    main()
    
