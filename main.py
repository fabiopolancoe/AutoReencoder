#!/usr/bin/env python3
from sys import argv
from sys import exit as bye

try:
    from subprocess import check_output
except:
    print("Could not import 'subprocess' module")
    bye(1)

print("Welcome to AutoReencoder!\n")

delete = input("Delete original files? [y/n] ")

print("Listing directory...")
dirlist = check_output("ls").decode().split("\n")
count = 0

if len(argv) == 3:
    print("Checking for input files with that extension...")
    for file in dirlist:
        if file.endswith(argv[1]):
            count += 1
            print("File found: \"" + file + "\". Reencoding to " + argv[2] + " format.")
            try:
                temp = check_output(["./ffmpeg", "-v", "error", "-i", file, file.replace(argv[1], argv[2])]).decode()
            except:
                print("An error occured:\n")
                raise
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
