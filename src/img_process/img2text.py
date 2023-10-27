"""
Methods for encoding text as an image
"""

from PIL import Image, PyAccess, ImageFilter
import hashlib
import typing


def hashImage(pixels: typing.List):
    return hashlib.sha256(str(pixels).encode()).hexdigest()


ColumnTypeDef = typing.Tuple[typing.List, str]


def processColumn(
    x: int, height: int, pix: PyAccess, blurredImagePix: PyAccess
) -> ColumnTypeDef:
    mask = []
    blurredMask = []
    # For each row
    for y in range(height):
        mask.append(pix[x, y])
        blurredMask.append(pix[x, y])

    return (mask, hashImage(blurredMask))


def getImageBitmasks(w, h, img: Image):
    masks = {}
    maskHashes = []

    blurredImage = img.filter(ImageFilter.GaussianBlur)
    pix = img.load()
    blurredImagePix = blurredImage.load()

    # For each column
    for x in range(w):
        (mask, maskHash) = processColumn(x, h, pix, blurredImagePix)
        masks[maskHash] = mask
        maskHashes.append(maskHash)

    return (masks, maskHashes)


def img2text(fileName: str):
    img = Image.open(fileName)
    blurredImage = img.filter(ImageFilter.GaussianBlur)

    # Get the dimensions of the image
    (w, h) = img.size

    masks = getImageBitmasks(w, h, img)
    return masks
