import sys
#import rogi 
from PIL import Image
from PIL.ExifTags import TAGS

def main():
    #https://www.thepythoncode.com/article/extracting-image-metadata-in-python

    # path to the image or video
    imagename = "photo/test.jpg"

    # read the image data using PIL
    image = Image.open(imagename)

    # extract EXIF data
    exifdata = image.getexif()

    # iterating over all EXIF data fields
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes 
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")

    """
    if(rogi.main):
        print("Kadrowanie poprawne")
    else:
        print("Kadrowanie niepoprawne")    
    """
if __name__ == "__main__":
    main()