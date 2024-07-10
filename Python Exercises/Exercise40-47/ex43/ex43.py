import os

def html(name,author,folders):
    file_path = "Exercise40-50\ex43\website\\"
    fullfile = file_path+name+"\index.html"
    fileOut = open(fullfile,"w")
    fileOut.write("<!DOCTYPE html>\n<html lang = en>\n<head>\n<meta name = \"article:author\" content=")
    fileOut.write(author)
    fileOut.write("\">\n")
    fileOut.write("<title>")
    fileOut.write(name)
    fileOut.write("</title>\n")
    fileOut.write("</head>\n<body>\n\n</body>\n</html>")
    output = "Created ./website/"+name+"/index.html"
    print(output)


def create(name, author, flagJS, flagCSS):
    starter = "./Exercise40-50/ex43/website"
    slash = '/'
    folders = starter+ slash + name
    print(folders)
    os.makedirs(folders)
    output = "Created ./website/"+name
    print(output)
    html(name,author,folders)
    if flagJS == True:
        JSfolder = folders +slash+"js/"
        os.mkdir(JSfolder)
        output = "Created ./website/"+name+"/js/"
        print(output)
    if flagCSS == True:
        CSSfolder = folders+slash+"css/"
        os.mkdir(CSSfolder)
        output = "Created ./website/"+name+"/css/"
        print(output)
    #os.mkdir(starter)


flagJS = False
flagCSS = False
slash = '\\'
print(slash)
name = input("What's the site name? ")
author = input("What's the Author's name? ")
JS = input("Do you want a folder for javascript? ")
if 'y' in JS.lower():
    flagJS = True
CSS = input("Do you want a folder for CSS? ")
if CSS.lower() == "y":
    flagCSS = True

print(flagCSS)
print(flagJS)

create(name,author,flagJS,flagCSS)
