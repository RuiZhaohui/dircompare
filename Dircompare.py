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

    #checks if a file exists if is does not creates it
    if os.path.exists("file.txt"):
        f = file("file.txt", "r+")
    else:
        f = file("file.txt", "w")

    var = "F:\\Python27\\Test"

    for filename in os.listdir(var):
        print filename
        filesize = os.path.getsize(filename)

        if filesize >= 1048576:
            print str(filesize / 1048576) + " MB" 
        elif filesize >= 1024:
            print str(filesize /1024) + "kb"
        else:
            print str(filesize) + "b"
        



#standard to call main function 
if __name__ == '__main__':
    main()
    
