"""
Methods for encoding text as an image
"""

from PIL import Image


def processColumn(x: int, height: int, pix):
    columnBitmask = 0b10
    # For each row
    for y in range(height):
        # Is the pixel black
        if pix[x, y] == (0, 0, 0, 255):
            columnBitmask |= 0b1

        if y + 1 < height:
            # Move the bitmask forward
            columnBitmask <<= 0b1

    return columnBitmask


def img2text(fileName: str):
    img = Image.open(fileName)

    # Get the dimensions of the image
    (w, h) = img.size

    pix = img.load()

    bitmasks = []

    # For each column
    for x in range(w):
        columnBitmask = processColumn(x, h, pix)
        bitmasks.append(columnBitmask)
    print(bitmasks)
    return " ".join(map(str, bitmasks))
