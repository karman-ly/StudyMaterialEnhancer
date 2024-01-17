import glob
import os

import fitz

import config
from enhancers import ImageData


def pdf_to_images() -> list[ImageData]:
    input_file = glob.glob(config.INPUT_DIR / "*.pdf")[0]

    doc = fitz.open(input_file)

    output_dir = config.OUTPUT_DIR / "images"
    os.makedirs(output_dir, exist_ok=True)

    res = []
    for i, page in enumerate(iter(doc)):
        pix = page.get_pixmap()
        output_path = output_dir / f"{i}.png"
        pix.save(output_path)
        res.append(ImageData.from_file(output_path))

    return res
