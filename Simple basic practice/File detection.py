import os
d = "C:\\Users\\aakas\\OneDrive\\Desktop\\p"
if os.path.exists(d):
    print("That location exists.")
    if os.path.isfile(d):
        print("This is a file")
    elif os.path.isdir(d):
        print("It is a directory.")
else:
    print("Location doesn't exist")
