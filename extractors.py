import fitz
from PIL import Image

import config
from enhancers import ImageData, TextData


def resize(file_path, base_width=None, base_height=None):
    img = Image.open(file_path)

    w_percent = (base_width / float(img.size[0])) if base_width is not None else 1
    h_percent = (base_height / float(img.size[1])) if base_height is not None else 1
    if base_width and not base_height:
        base_height = int((float(img.size[1]) * float(w_percent)))
    elif base_height and not base_width:
        base_width = int((float(img.size[0]) * float(h_percent)))
    else:
        base_width, base_height = img.size

    img = img.resize((base_width, base_height), Image.LANCZOS)

    img.save(file_path)


def pdf_to_images() -> list[ImageData]:
    doc = fitz.open(config.INPUT_FILE)

    res = []
    for i, page in enumerate(iter(doc), start=1):
        output_path = config.IMAGES_OUTPUT_DIR / f"{i}.jpg"
        if not output_path.exists():
            pix = page.get_pixmap()
            if config.IMAGE_RESOLUTION is not None:
                resize(output_path)
            pix.save(output_path)
        res.append(ImageData.from_file(output_path))

    return res


def read_instructions() -> TextData:
    with open(config.INSTRUCTIONS_FILE, "r", encoding="utf-8") as f:
        return TextData(f.read())
