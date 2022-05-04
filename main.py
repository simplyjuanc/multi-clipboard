import sys
import clipboard
import json


def save_item(cache, keyword, item):
    with open(cache, 'a') as clipb:
        json.dump({keyword : item}, clipb)


def load_item(cache, keyword, item):
    pass

def del_item(cache, keyword, item):
    pass




if len(sys.argv) != 2:
    print('wrong argv length')




data = clipboard.paste()
CACHE = "PATH_SOMEWHERE"
KEYWORD = sys.argv[1]


command = input("What would you like to do? (save/list/load/del)\n")
if command == "list":
    save_item(cache=CACHE, keyword=KEYWORD, item=data)
    
    print('list')
elif command == "save":
    print('save')
elif command == "load":
    print('load')
elif command == "del":
    
    print('del')
else:
    print("Error")

