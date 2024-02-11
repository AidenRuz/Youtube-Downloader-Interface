# pip install pytube
from pytube import YouTube
from pathlib import Path
from os import path

# Used to add color to printed text in terminal
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Declarations
filePath = str(Path(__file__).parent.absolute())
currentPath = str(Path.cwd().absolute())
audioPath = "\\Downloads\\audio"
videoPath = "\\Downloads\\video"


# List all the downloadable streams from the link
def selectStream(youtubeObject):
    downloads = []
    # Store and output list of available streams
    for index, item in enumerate(youtubeObject):
        downloads.append(item)
        print(str(index) + ": " + str(item))
    print(color.YELLOW + "Select which version you would like to download." + color.END)
    # Input validation
    while(True):
        streamIndex = int(input(color.CYAN + "Enter response here: " + color.END))
        if streamIndex < 0 or streamIndex > (len(downloads) - 1):
             print("Error: Please enter a value between the range shown above.")
        else:
            break
    
    return youtubeObject[streamIndex]


# Takes user input and passes it to the main download function
def main():
    print(color.RED + color.BOLD + "Welcome to Youtube-Downloader-Interface!" + color.END)
    print(color.YELLOW + "Where would you like to download?" + color.END)
    print(color.YELLOW + "1: Current Working Directory (" + currentPath + ")" + color.END)
    print(color.YELLOW + "2: Where the python file was run from (" + filePath + ")" + color.END)
    print(color.YELLOW + "3: Enter path manually")
    while(True):
        value = input(color.CYAN + "Enter response here: " + color.END)
        if value == "1":
            selectedPath = currentPath
            break
        elif value == "2":
            selectedPath = filePath
            break
        elif value == "3":
            # Takes custom path and ensures it exists
            exists = False
            while(exists == False):
                selectedPath = input(color.CYAN + "Enter path here: " + color.END)
                exists = path.exists(selectedPath)
                if exists == True:
                    print(color.GREEN + "Path Accepted." + color.END)
                    break
                else:
                    print(color.RED + "Path Rejected." + color.END)
            break
        else:
            print(color.RED + "Error: Please enter a value of 1,2 or 3." + color.END)
    
    
    
    link = input(color.CYAN + "Enter the YouTube video URL: " + color.END)
    print(color.YELLOW + "Would you like to download audio or video?" + color.END)
    print(color.YELLOW + "1: Audio" + color.END)
    print(color.YELLOW + "2: Video" + color.END)
    # Input validation
    while(True):
        selector = int(input(color.CYAN + "Enter response here: " + color.END))
        if (selector > 0) and (selector < 3):
            break
        else:
            print(color.RED + "Error: Please enter a value of 1 or 2." + color.END)
    
    
    # Setup pytube object
    youtubeObject = YouTube(link)
    
    if selector == 1:
        youtubeObject = youtubeObject.streams.filter(only_audio=True)
        if value != 3:
            selectedPath += audioPath
    else:
        youtubeObject = youtubeObject.streams.filter(file_extension="mp4")
        if value != 3:
            selectedPath += videoPath
    
    
    # List streams and allow user to select which stream to download
    youtubeObject = selectStream(youtubeObject)
    
    # Attempt download
    try:
        if selector == 1:
            youtubeObject.download(selectedPath)
        else:
            youtubeObject.download(selectedPath)
    except Exception as e:
        print(color.RED + "Error: " + str(e) + color.END)
        return
    print(color.GREEN + "Download completed successfully." + color.END)


# Execute the program
main()