from random import randint
from clint.textui import progress
import requests


def downloadFileFromUrl(url, extension, folderPath):
    filename = str(randint(100000, 999999)) + extension
    r = requests.get(url, stream=True)
    path = f"./{folderPath}/{filename}"
    with open(path, "wb") as f:
        total_length = int(r.headers.get("content-length"))
        for c in progress.bar(
            r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1
        ):
            f.write(c)
            f.flush()
    return filename


if __name__ == "__main__":
    # throw a RuntimeError if file ran on it's own
    raise RuntimeError("Please don't run this code on it's own.")
