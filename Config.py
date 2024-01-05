import json, os

if not os.path.exists("./config.json"):
    raise RuntimeError(
        "Please create a config.json file, read docs for more information."
    )

if __name__ == "__main__":
    raise RuntimeError("Please don't run this code on it's own.")

with open("config.json") as f:
    data = json.load(f)

class Discord:
    images = data["discord"]["imageChannelID"]
    videos = data["discord"]["videoChannelID"]
    source = data["discord"]["sourceChannelID"]
    token = data["discord"]["token"]

class Drive:
    images = data["googleDrive"]["imagesFolderID"]
    videos = data["googleDrive"]["videosFolderID"]
    
class App:
    def folderName():
        try:
            return data["app"]["downloadFolderName"]
        except:
            return "temp"

    def checkKeepFiles():
        try:
            return data["app"]["keepDownloads"]
        except:
            return True

    downloadFolderName = folderName()
    keepDownloads = checkKeepFiles()
