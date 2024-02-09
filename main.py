from pytube import YouTube
from pathlib import Path

# Declarations
link = ""
selector = 2
audioPath = str(Path(__file__).parent.absolute()) + "\\Downloads\\audio"
videoPath = str(Path(__file__).parent.absolute()) + "\\Downloads\\video"


# Main download function
def download(link, selector):
    youtubeObject = YouTube(link)
    
    if selector == 1:
        youtubeObject = youtubeObject.streams.filter(only_audio=True)
    else:
        youtubeObject = youtubeObject.streams.filter(file_extension="mp4")
    
    # List streams and allow user to select which stream to download
    youtubeObject = selectStream(youtubeObject)
    
    try:
        if selector == 1:
            youtubeObject.download(audioPath)
        else:
            youtubeObject.download(videoPath)
    except:
        print("An error has occurred.")
        return
    print("Download completed successfully.")


# List all the downloadable streams from the link
def selectStream(youtubeObject):
    downloads = []
    # Store and output list of available streams
    for index, item in enumerate(youtubeObject):
        downloads.append(item)
        print(str(index) + ": " + str(item))
    print("Select which version you would like to download: ")
    # Input validation
    while(True):
        streamIndex = int(input())
        if streamIndex < 0 or streamIndex > (len(downloads) - 1):
             print("Error: Please enter a value between the range shown above.")
        else:
            break
    
    return youtubeObject[streamIndex]


# Takes user input and passes it to the main download function
def main():
    global selector
    print("Enter the YouTube video URL: ")
    link = input()
    print("Would you like to download audio or video? (Default Video)")
    print("1: Audio")
    print("2: Video")
    # Input validation
    while(True):
        value = input()
        if value == "1":
            selector = 1
            break
        elif value == "2":
            selector = 2
            break
        else:
            print("Error: Please enter a value of 1 or 2.")
    download(link, selector)


# Executes the program
main()