import sys
import clipboard
import json

data = clipboard.paste()


if len(sys.argv) != 2:
    print('wrong argv length')

command = input("What would you like to do? (save/list/load/del)\n")
if command == "list":
    print('list')
elif command == "save":
    print('save')
elif command == "load":
    print('load')
elif command == "del":
    
    print('del')
else:
    print("Error")

