from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


def auth():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return drive


def uploadToDrive(folder, path, filename, drive):
    f = drive.CreateFile({"parents": [{"id": folder}], "title": filename})
    f.SetContentFile(path)
    f.Upload()
    print(f"Uploaded {filename} to Google Drive")
    f = None


if __name__ == "__main__":
    raise RuntimeError("Please don't run this code on it's own.")
