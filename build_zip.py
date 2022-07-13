import zipfile
import os

class Zipping:
    def __init__(self, path):
        self.archive_name = "pygame_novel-v2.0pre1"
        self.archive_ext = ".zip"
        self.archive = zipfile.ZipFile(self.archive_name + self.archive_ext, "w")
        for root, dirs, files in os.walk(path):
            for file in files:
                data = os.path.join(root, file)
                self.archive.write(data, os.path.relpath(data, os.path.join(path, '..')))

if __name__ == "__main__":
    output_zip = Zipping('pygame-novel')
    
