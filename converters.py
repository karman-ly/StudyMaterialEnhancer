import glob
import os

import fitz

import config
from enhancers import ImageData


def resize(pixels):
    print(type(pixels))


def pdf_to_images() -> list[ImageData]:
    input_file = glob.glob(str(config.INPUT_DIR / "*.pdf"))[0]

    doc = fitz.open(input_file)

    images_output_dir = config.OUTPUT_DIR / "images"
    os.makedirs(images_output_dir, exist_ok=True)

    res = []
    for i, page in enumerate(iter(doc)):
        pix = page.get_pixmap()
        if config.IMAGE_RESOLUTION is not None:
            pix = resize(pix)
        output_path = images_output_dir / f"{i}.jpg"
        pix.save(output_path)
        res.append(ImageData.from_file(output_path))

    return res


convert = pdf_to_images
