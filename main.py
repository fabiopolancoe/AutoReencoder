#!/usr/bin/env python3
try:
    import os
    from sys import argv
    from sys import exit as bye
    from subprocess import check_output
    
    print("Welcome to AutoReencoder!\n")
    
    count = 0

    if len(argv) == 3:
        print("Make sure ffmpeg is installed and added to $PATH")
        delete = input("Delete original files? [y/n] ")
        print("Listing directory...")
        dirlist = check_output("ls").decode().split("\n")
        print("Checking for input files with that extension...")
        for file in dirlist:
            if file.endswith(argv[1]):
                count += 1
                print("File found: \"" + file + "\". Reencoding to " + argv[2] + " format.")
                try:
                    tmp = check_output(["ffmpeg", "-v", "quiet", "-i", file, file.replace(argv[1], argv[2])]).decode()        
                except Exception as e:
                    print("An error occured:\n" + str(e))
                else:
                    print("File reencoded succesfully!")

                if delete.lower() == "y":
                    print("Deleting original file")
                    temp = check_output(["rm", file])
        print("Finished all reencodings.\nTotal: " + str(count) + "\nBye!")
        bye(0)            
    else:
        print("Pass both input and output file extension as arguments please")
        bye(1)
except KeyboardInterrupt:
    print("Okay dude, don't be rude, bye!")
    bye(0)
