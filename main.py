from datetime import datetime
from os import listdir
from datetime import datetime
import piexif
import os
from os.path import isfile, join

mediaFolder = "/Users/eamonbarkhordarian/Desktop/home-videos-clips-converted-by-nvidia-compressed/DATED_VIDEOS/02-06-2001"

if __name__ == '__main__':
    ## count number of photos found
    listOfFolders = [x[0] for x in os.walk(mediaFolder)]
    if len(listOfFolders) > 1:
        listOfFolders.pop(0)
    count = 0
    for folderPath in listOfFolders:
        folderName = os.path.basename(folderPath)
        filesInFolder = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
        parsedate = datetime.strptime(folderName, '%m-%d-%Y')
        secondsCount = 0
        parsedate.replace(hour=00, minute=00, second=secondsCount)
        print(parsedate)
        print("folder name:" + folderName)
        print("month: " + str(parsedate.month))
        print("day: " + str(parsedate.day))
        print("year: " + str(parsedate.year))
        for file in filesInFolder:
            print("folder path: " + folderPath)
            print("folder name: " + folderName)
            print("file: " + file)
            if ".DS_Store" in file or "Thumbs.db" in file or "Picasa.ini" in file:
                print("yes")
                continue
            fileAbsolutePath = os.path.join(folderPath, file)
            print("file absolute path: " + fileAbsolutePath)
            exif_dict = piexif.load(fileAbsolutePath)
            newExifDate = parsedate.strftime("%Y:%m:%d %H:%M:%S")
            exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = newExifDate
            exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = newExifDate
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, fileAbsolutePath)
            print("completed")
            count = count + 1
            print("")

    # print count
    # fileCount = len(listOfFiles)
    # print fileCount

    # ## create datetimeString from JPG filename
    # for jpg in os.listdir(jpgFolder):
    #     filepath = jpgFolder + "\\" + jpg
    #
    #     parsedate = datetime.strptime(jpg[0:16], "%Y-%m-%d-%H-%M-%S")
    #     ## change exif datetimestamp for "Date Taken"
    #     exif_dict = piexif.load(filepath)
    #     newExifDate = parsedate.strftime("%Y:%m:%d %H:%M:%S")
    #     exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = newExifDate
    #     exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = newExifDate
    #     exif_bytes = piexif.dump(exif_dict)
    #     piexif.insert(exif_bytes, filepath)
    # # Press the green button in the gutter to run the script.
