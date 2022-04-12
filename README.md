iPhone-Images-EXIF-extractor.py quickly extracts certain iPhone pertinent JPEG EXIF data. Pertinent data in this case is all datestamp information as well as make and model.
    
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
