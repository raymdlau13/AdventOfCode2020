import os

sourcePath="/users/kingwanlau/dev"
destPath="/users/kingwanlau/bkup"
files = [ os.path.join(sourcePath,f) for f in os.listdir(sourcePath) if os.path.isfile(os.path.join(sourcePath,f)) ]
print(files)
for file in files:
    print(file + ' - ' + os.path.basename(file))
    if not os.path.exists(destPath + os.path.basename(file)):
        print("Here")