A discord bot to upload message attachments to Google Drive


### Create a config.json file

Create a config.json file in the same directory as Config.py and it should look like this
```json
{
    "googleDrive": {
        "imagesFolderID": "PUT YOUR OWN DRIVE FOLDER ID",
        "videosFolderID": "PUT YOUR OWN DRIVE FOLDER ID"
    },
    "discord": {
        "imageChannelID": 0000000000000000000,
        "videoChannelID": 0000000000000000000,
        "sourceChannelID": 0000000000000000000,
        "token": "YOUR BOT TOKEN HERE"
    },
    "app": {
        "downloadFolderName": "Downloads",
        "keepDownloads": true
    }
}
```

**downloadFolderName** is just the name of the folder that files are going to get downloaded at.

**keepDownloads** is a boolean value to decide if you want to keep files after downloading and uploading them or not. Can be either true or false.

## FAQ

#### **How to get your Drive folder ID**

[Read this](https://pythonhosted.org/PyDrive/filelist.html#get-all-files-which-matches-the-query) to get your google drive folder ID.

#### **How to get your Discord channel ID**

You can get your discord channel ID by simply right clicking on a text channel and clicking on **Copy channel ID** if you can't see that option enable Developer mode through your settings. You can put the same ID on both image and video.

#### **How to get your Discord bot token**

You can get your bot token through Discord Developer Portal


