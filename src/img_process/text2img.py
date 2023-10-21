from PIL import Image


def text2img(bitmaskString: str):
    bitmasks = list(map(int, bitmaskString.strip().split(" ")))

    # Get the dimensions of the image
    w = len(bitmasks)
    h = len(f"{bitmasks[0]:b}") - 1

    # Create a new image
    img = Image.new("RGBA", (w, h))
    img.getpixel((0, 0))

    for x in range(w - 1, -1, -1):
        # Get the bitmask
        bitmask = bitmasks[x]

        for y in range(h - 1, -1, -1):
            # If the bitmask is on use a black pixel
            if bitmask & 0b1 == 0b1:
                img.putpixel((x, y), (0, 0, 0, 255))
            # Otherwise use a white pixel
            else:
                img.putpixel((x, y), (255, 255, 255, 255))

            # Remove the flag from the bitmask
            bitmask >>= 0b1

    return img
