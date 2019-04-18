import re,os,argparse
osdir = os.listdir()
defchars = 12
oldlist = []
ext = ["mp4", "webm"]

def getextension(string):
    extension = re.split('\.', string)
    extension = extension[len(extension) - 1]
    return extension

#e as in experimental
def eremoveid(string, num):
    extension = getextension(string)
    string = string.replace("." + extension, "")
    string = string[:-num]
    string = f"{string}.{extension}"
    return string

def saveold(namelist):
    oldnames = open("oldnames.txt", "a", encoding="utf-8")
    for i in range(len(namelist)):
        name = str(namelist[i])
        oldnames.write(f"{name}\n")
    oldnames.close()

def replacenames(filedir, num, nosave):
        for i in range(len(filedir)):
            if getextension(filedir[i]) in ext:
                oldlist.append(filedir[i])
                try:
                    os.rename(filedir[i], eremoveid(osdir[i], num))
                except FileExistsError:
                    print(f"{filedir[i]} already exists. Skipping...")
        if not nosave:
            saveold(oldlist)
            
        return True
    
def listexists():
    try:
        open("oldnames.txt", "r")
        return True
    except:
        return False
    
def main(args):
    if not args.ignore:
        if listexists():
            print("Warning! File rename has been already been done to this folder. To continue either delete/rename oldnames.txt or use the -i flag")

        else:
            replacenames(osdir, args.chars, args.skip)

    else:
        replacenames(osdir, args.chars, args.skip)

parser = argparse.ArgumentParser(description='File renaming help tool.')
parser.add_argument('-i', '--ignore', help='Ignore the filename list check.', action='store_true')
parser.add_argument('-s', '--skip', help='Skips creating the filename list creation.', action='store_true')
parser.add_argument('-c', metavar='CHARS', type=int, default=12, help='The number of characters to remove.')
#parser.add_argument('-d', '--directory', metavar='DIRECTORY', type=str, help='Perform the rename at a specified folder.')
args = parser.parse_args()

main(args)
