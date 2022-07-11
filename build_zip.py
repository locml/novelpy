import os
import zipfile
    
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))

with zipfile.ZipFile('novelpy-1.0b1.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir('novelpy', zipf)
