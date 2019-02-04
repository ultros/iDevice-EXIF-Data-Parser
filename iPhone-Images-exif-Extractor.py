#!/usr/bin/env python

'''iPhone-Images-EXIF-extractor.py; December 17th, 2012
contact@nsa.sh, realjesseshelley@gmail.com

    iPhone-Images-EXIF-extractor.py quickly extracts certain
    iPhone pertinent JPEG EXIF data. Pertinent data in this
    case is all datestamp information as well as make and
    model.

    1. First EXIF data is extracted from an image
    using the Python Imaging Library (PIL) and
    the data is then processed into an array for
    ease in searching.

    2. Print date and time to stdout
    in tab delimited format.

EXIF key values handled:

    DateTime - Last modification date. This value may change
    if the image was edited in software which would update
    this EXIF value/key.

    DateTimeOriginal - When image data was first generated.

    DateTimeDigitized - When image data was first stored.

    Make/Model


'''

import sys, os
from PIL import Image
from PIL.ExifTags import TAGS

def decodeExif(imageName):
    '''Extracts EXIF data from image.
    Arguments:

    imageName - Image filename to extract
    EXIF data from.

    Returns an array with decoded EXIF tags.'''

    exifData = {}
    try:
        imageFile = Image.open(imageName)
        eInfo = imageFile._getexif()
        for (tag, value) in eInfo.items():
            # Decode numeric EXIF tags.
            dTag = TAGS.get(tag, tag)
            ###print dTag
            exifData[dTag] = value
    except:
        pass

    # Return decoded EXIF array.
    return exifData

def getKeyData(exifData, keyString):
    '''Returns value of keyString
    Arguments:

    exifData - Decoded EXIF data array
    keyString - EXIF key in string format

    If keyString does not exist, return
    "None"'''

    try:
        if exifData[keyString]:
          return exifData[keyString]
    except:
        return 'None'


print "Image Name\tLast Modified\tDate Image Taken\tDate Image Digitized\tCamera Manufacturer\tCamera Model"

files = [ file for file in os.listdir('.') if os.path.isfile(file)]

for file in files:
    eData = decodeExif(file)
    print file,'\t', \
    getKeyData(eData, 'DateTime'),'\t', \
    getKeyData(eData, 'DateTimeOriginal'),'\t', \
    getKeyData(eData, 'DateTimeDigitized'),'\t', \
    getKeyData(eData, 'Make'),'\t', \
    getKeyData(eData, 'Model')
