from calendar import c
import os


# ***Defining the command for ignoring the happening of more than 1 folder at the same time.***
def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# ***Defining the command for shifting the files into the appropriate folder***
def shift(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")

if __name__ == '__main__':

    files = os.listdir()
    files.remove("Folder_cleaning.py")   # for removing this code file from list and to keep it out of any folder for it's proper functioning

    # Create the folders 
    createIfNotExists('Docs')
    createIfNotExists('Images')
    createIfNotExists('Medias')
    createIfNotExists('Zips')
    createIfNotExists('Codes')
    createIfNotExists('Others')

    # Define the different file extensions to put in the respective folders

    docExts = [".docx", ".pdf", ".doc", ".txt", ".pptx",".ppt", ".xlsx", ".srt"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    imgExts= [".png",".jpg",".jpeg",".gif", ".wmf"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    mediaExts = [".mp3",".mp4",".wav", ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    zipExts = [".rar",".zip"]
    zips = [file for file in files if os.path.splitext(file)[1].lower() in zipExts]

    codeExts = [".py", ".m", ".json", ".dwxmz"]
    codes = [file for file in files if os.path.splitext(file)[1].lower() in codeExts]

    others = []   # Files with extensions other than defined above will be sent to "others" folder 
    for file in files:
        exts = os.path.splitext(file)[1].lower()
        if (exts not in docExts) and (exts not in codeExts) and (exts not in imgExts) and (exts not in mediaExts) and (exts not in zipExts) and os.path.isfile(file):
            others.append(file)


    #***Command to Shift the files to their repective folders according to their extensions.

    shift("Docs", docs)
    shift("Images", images)
    shift("Zips", zips)
    shift("Medias", medias)
    shift("Codes", codes)
    shift("Others", others)


# ***********************************************END*****************************************************










