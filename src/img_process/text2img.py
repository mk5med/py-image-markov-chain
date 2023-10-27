"""
Methods for decoding text as an image
"""

from PIL import Image
import typing


def text2img(bitmaskString: str, masks: typing.Dict[str, typing.Any]):
    maskHashes = bitmaskString.strip().split(" ")

    # Get the dimensions of the image
    w = len(maskHashes)
    h = len(masks[maskHashes[0]])

    # Create a new image
    img = Image.new("RGBA", (w, h))
    img.getpixel((0, 0))

    for x in range(w):
        pixels = masks[maskHashes[x]]
        for y in range(h):
            img.putpixel((x, y), pixels[y])

    return img
