import discord, Config, os
import Folder, Downloader, Drive


def discordClient():
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    drive = Drive.auth()

    @client.event
    async def on_ready():
        clear()
        sourceChannelName = client.get_channel(Config.Discord.source).name
        print(f"Listening for posts on channel #{sourceChannelName}")

    @client.event
    async def on_message(message):
        count = 0
        clear()
        attachmentSize = len(message.attachments)
        if message.channel.id == Config.Discord.source and attachmentSize != 0:
            keepFiles = Config.App.keepDownloads
            Folder.createFolder(Config.App.downloadFolderName)
            for attachment in message.attachments:
                mediaType = attachment.content_type.split("/")[0]
                if mediaType == "image" or mediaType == "video":
                    url = attachment.url
                    extension = "." + attachment.filename.split(".")[-1]
                    filename = Downloader.downloadFileFromUrl(
                        url, extension, Config.App.downloadFolderName
                    )
                    count += 1
                    print(f"[{count}/{attachmentSize}]")
                    await messageFiles(client, mediaType, filename)
                    path = f"./{Config.App.downloadFolderName}/{filename}"
                    folder = (
                        Config.Drive.images
                        if mediaType == "image"
                        else Config.Drive.videos
                    )
                    clear()
                    Drive.uploadToDrive(folder, path, filename, drive)
            if not keepFiles:
                Folder.removeFolder(Config.App.downloadFolderName)
            await message.delete()

    client.run(Config.Discord.token)


async def messageFiles(client, mediaType, filename):
    channelId = Config.Discord.images if mediaType == "image" else Config.Discord.videos
    channel = client.get_channel(channelId)
    await channel.send(
        file=discord.File(f"./{Config.App.downloadFolderName}/{filename}")
    )


def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


if __name__ == "__main__":
    discordClient()
