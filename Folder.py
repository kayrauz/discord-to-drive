import os
from shutil import rmtree


def createFolder(folderPath):
    folder = f"./{folderPath}"
    if not os.path.exists(folder):
        try:
            os.mkdir(folder)
        except OSError as e:
            print(f"Error creating folder: {e}")


def removeFolder(folderPath):
    folder = f"./{folderPath}"
    try:
        os.rmdir(folder)
    except OSError as e:
        # 41 error no = directory not empty error
        if e.errno == 41:
            rmtree(folder)
        else:
            print(f"Error removing folder: {e}")


if __name__ == "__main__":
    raise RuntimeError("Please don't run this code on it's own.")
